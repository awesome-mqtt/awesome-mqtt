#!/usr/bin/env python3
"""Build README.md from list.md, leaving out entries that fail the quality gate.

list.md is the file contributors send pull requests against. This script copies
it to README.md line by line and drops every list entry whose main link fails
one of these checks:

* GitHub repositories need at least MIN_STARS stars and a commit on the default
  branch within the last MAX_INACTIVE_DAYS days. Archived repositories and
  repositories that no longer exist fail as well.
* All other links must not be dead (404/410, unknown host, refused connection).
  Responses that are ambiguous (403/429/5xx/timeouts; many sites block bots)
  do NOT remove an entry; they are only listed in the report.

Every GitHub repository link in README.md gets its star count appended (<small>★&nbsp;1.2k</small>).

Entries can be exempted by adding their URL to scripts/quality-gate-exceptions.txt.

Dropped and uncertain entries are written to excluded.md so contributors can see
why their entry does not show up in the README.

Usage: GITHUB_TOKEN=... python3 scripts/build_readme.py [--source list.md]
       [--readme README.md] [--report excluded.md]
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import json
import os
import re
import socket
import ssl
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

MIN_STARS = 10
MAX_INACTIVE_DAYS = 2 * 365

ROOT = Path(__file__).resolve().parent.parent
EXCEPTIONS_FILE = ROOT / "scripts" / "quality-gate-exceptions.txt"

ITEM_RE = re.compile(r"^\s*[-*] \[(?P<name>[^\]]+)\]\((?P<url>[^)\s]+)\)")
GITHUB_RE = re.compile(
    r"^https?://(?:www\.)?github\.com/(?P<owner>[A-Za-z0-9-_.]+)/(?P<repo>[A-Za-z0-9-_.]+?)(?:\.git)?(?:[/#?].*)?$"
)
LINK_RE = re.compile(r"\]\((?P<url>https?://[^)\s]+)\)")
# GitHub URL suffixes after owner/repo that still point at the repository itself
# (gets a star count); anything else (wiki, issues, ...) is left alone.
REPO_PAGE_SUFFIX = re.compile(r"^(?:\.git)?/?(?:(?:tree|blob)/.*)?(?:#.*)?$")
# github.com/<first>/... paths that are not repositories
GITHUB_NON_REPO = {"orgs", "topics", "sponsors", "marketplace", "features", "collections", "apps"}

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/130.0 Safari/537.36 awesome-mqtt-link-check"
)

PASS, FAIL, UNSURE = "pass", "fail", "unsure"


@dataclass
class Entry:
    line_no: int
    name: str
    url: str
    section: str
    status: str = PASS
    reasons: list[str] = field(default_factory=list)


# --------------------------------------------------------------------------- parsing


def parse_entries(lines: list[str]) -> list[Entry]:
    entries = []
    section = ""
    for i, line in enumerate(lines):
        if line.startswith("#"):
            section = line.lstrip("#").strip()
            continue
        m = ITEM_RE.match(line)
        if not m or not m.group("url").startswith(("http://", "https://")):
            continue  # table of contents (#anchors), irc:// etc.
        entries.append(Entry(i, m.group("name"), m.group("url"), section))
    return entries


def github_repo(url: str) -> tuple[str, str] | None:
    m = GITHUB_RE.match(url)
    if not m or m.group("owner").lower() in GITHUB_NON_REPO:
        return None
    return m.group("owner"), m.group("repo")


def load_exceptions() -> set[str]:
    if not EXCEPTIONS_FILE.exists():
        return set()
    out = set()
    for line in EXCEPTIONS_FILE.read_text().splitlines():
        line = line.split(" #", 1)[0].strip()  # "<url>  # why it is exempt"
        if line and not line.startswith("#"):
            out.add(line.rstrip("/"))
    return out


# --------------------------------------------------------------------------- GitHub


def graphql(token: str, query: str) -> dict:
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query}).encode(),
        headers={"Authorization": f"bearer {token}", "User-Agent": "awesome-mqtt-quality-gate"},
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code < 500 or attempt == 2:
                raise
            time.sleep(5 * (attempt + 1))
    raise RuntimeError("unreachable")


def rest_repo(token: str, owner: str, repo: str) -> dict | None:
    """Fallback for renamed/transferred repos: the REST API follows redirects."""
    req = urllib.request.Request(
        f"https://api.github.com/repos/{owner}/{repo}",
        headers={"Authorization": f"bearer {token}", "User-Agent": "awesome-mqtt-quality-gate"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        if e.code in (404, 451):
            return None
        raise


REPO_FIELDS = """
  nameWithOwner stargazerCount isArchived
  defaultBranchRef { target { ... on Commit { committedDate } } }
"""


def fetch_github(keys: list[tuple[str, str]], token: str) -> dict[tuple[str, str], dict | None]:
    """Fetch stars/archived/last commit for (owner, repo) keys; None = not found."""
    info: dict[tuple[str, str], dict | None] = {}
    for start in range(0, len(keys), 50):
        chunk = keys[start : start + 50]
        parts = [
            f'r{i}: repository(owner: {json.dumps(o)}, name: {json.dumps(r)}) {{{REPO_FIELDS}}}'
            for i, (o, r) in enumerate(chunk)
        ]
        data = graphql(token, "query {" + "\n".join(parts) + "}").get("data") or {}
        for i, key in enumerate(chunk):
            info[key] = data.get(f"r{i}")

    for key in keys:
        if info[key] is None:
            # Maybe renamed or moved; the REST API follows the redirect.
            rest = rest_repo(token, *key)
            if rest is not None:
                owner, name = rest["full_name"].split("/")
                info[key] = (graphql(
                    token,
                    f'query {{ r: repository(owner: {json.dumps(owner)}, name: {json.dumps(name)}) {{{REPO_FIELDS}}} }}',
                ).get("data") or {}).get("r")
    return info


def last_commit(repo: dict) -> dt.datetime | None:
    target = (repo.get("defaultBranchRef") or {}).get("target") or {}
    last = target.get("committedDate")
    return dt.datetime.fromisoformat(last.replace("Z", "+00:00")) if last else None


def gate_reasons(repo: dict | None, min_stars: int = MIN_STARS, max_inactive_days: int = MAX_INACTIVE_DAYS) -> list[str]:
    """Why a repository fails the quality gate (empty list = passes)."""
    if repo is None:
        return ["repository not found"]
    reasons = []
    if repo["isArchived"]:
        reasons.append("repository is archived")
    if repo["stargazerCount"] < min_stars:
        reasons.append(f"{repo['stargazerCount']} stars (< {min_stars})")
    last = last_commit(repo)
    cutoff = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=max_inactive_days)
    if last is None:
        reasons.append("no commits found")
    elif last < cutoff:
        reasons.append(f"last commit {last.date()} (> {max_inactive_days // 365} years ago)")
    return reasons


def repo_key(url: str) -> tuple[str, str]:
    owner, repo = github_repo(url)
    return owner.lower(), repo.lower()


def check_github(entries: list[Entry], info: dict[tuple[str, str], dict | None]) -> None:
    for e in entries:
        reasons = gate_reasons(info[repo_key(e.url)])
        if reasons:
            e.status, e.reasons = FAIL, reasons


# --------------------------------------------------------------------------- other links


def probe(url: str) -> tuple[str, str]:
    """Return (status, reason) for a single URL."""
    ctx = ssl.create_default_context()
    last = (UNSURE, "no response")
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": USER_AGENT, "Accept": "*/*"})
        try:
            with urllib.request.urlopen(req, timeout=25, context=ctx) as r:
                return PASS, f"HTTP {r.status}"
        except urllib.error.HTTPError as e:
            if e.code in (404, 410):
                last = (FAIL, f"HTTP {e.code}")
            else:
                last = (UNSURE, f"HTTP {e.code}")
            # Many servers answer HEAD wrongly, so always retry with GET.
        except urllib.error.URLError as e:
            reason = e.reason
            if isinstance(reason, socket.gaierror):
                return FAIL, "host not found"
            if isinstance(reason, ConnectionRefusedError):
                return FAIL, "connection refused"
            if isinstance(reason, ssl.SSLCertVerificationError):
                return FAIL, f"TLS certificate error ({reason.verify_message})"
            last = (UNSURE, f"{type(reason).__name__}: {reason}")
        except (TimeoutError, socket.timeout):
            last = (UNSURE, "timeout")
        except Exception as e:  # noqa: BLE001 - report anything odd as unsure
            last = (UNSURE, f"{type(e).__name__}: {e}")
    return last


def check_links(entries: list[Entry]) -> None:
    urls = sorted({e.url for e in entries})

    def probe_twice(url: str) -> tuple[str, str]:
        result = probe(url)
        if result[0] != PASS:  # one retry, so a short hiccup doesn't drop an entry
            time.sleep(10)
            result = probe(url)
        return result

    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as pool:
        results = dict(zip(urls, pool.map(probe_twice, urls)))
    for e in entries:
        status, reason = results[e.url]
        if status != PASS:
            e.status, e.reasons = status, [reason]


# --------------------------------------------------------------------------- output


def slug(heading: str) -> str:
    """GitHub's heading anchor: lowercase, drop punctuation, spaces -> dashes."""
    return re.sub(r"[^\w\- ]", "", heading.strip().lower()).replace(" ", "-")


def render(lines: list[str], drop: set[int]) -> list[str]:
    """Remove dropped entries, then headings whose section lost all its entries
    (including nested sub-sections), together with their table-of-contents line."""
    headings = [(i, len(l) - len(l.lstrip("#"))) for i, l in enumerate(lines) if l.startswith("#")]
    removed: set[int] = set(drop)
    empty_anchors: set[str] = set()
    for n, (start, level) in enumerate(headings):
        end = next((i for i, lv in headings[n + 1 :] if lv <= level), len(lines))
        items = [i for i in range(start, end) if ITEM_RE.match(lines[i])]
        if items and all(i in drop for i in items):
            # Section had entries and all are gone: drop heading and its own text
            # (up to the next heading), nested headings are handled by their own pass.
            own_end = next((i for i, _ in headings[n + 1 :]), len(lines))
            removed.update(range(start, own_end))
            empty_anchors.add(slug(lines[start].lstrip("#")))
    toc_re = re.compile(r"^\s*[-*] \[[^\]]+\]\(#(?P<anchor>[^)]+)\)\s*$")
    out = []
    for i, line in enumerate(lines):
        if i in removed:
            continue
        m = toc_re.match(line)
        if m and m.group("anchor") in empty_anchors:
            continue
        out.append(line)
    return out


def repo_page_key(url: str) -> tuple[str, str] | None:
    """(owner, repo) if the URL points at a GitHub repository itself, else None."""
    m = GITHUB_RE.match(url)
    if not m or not github_repo(url):
        return None
    if not REPO_PAGE_SUFFIX.match(url[m.end("repo") :]):
        return None
    return repo_key(url)


def list_item_repo_keys(lines: list[str]) -> set[tuple[str, str]]:
    """All repositories linked from list items, main link or inside the description."""
    return {
        key
        for line in lines
        if ITEM_RE.match(line)
        for m in LINK_RE.finditer(line)
        if (key := repo_page_key(m.group("url")))
    }


def format_stars(n: int) -> str:
    if n < 1000:
        return str(n)
    if n < 10000:
        return f"{n / 1000:.1f}k".replace(".0k", "k")
    return f"{round(n / 1000)}k"


def add_stars(lines: list[str], info: dict[tuple[str, str], dict | None]) -> list[str]:
    """Append the star count after every GitHub repository link in list items,
    same markup as on github.com/hobbyquaker: <small>★&nbsp;1.2k</small>."""

    def annotate(m: re.Match) -> str:
        key = repo_page_key(m.group("url"))
        repo = info.get(key) if key else None
        if not repo:
            return m.group(0)
        return f"{m.group(0)} <small>★&nbsp;{format_stars(repo['stargazerCount'])}</small>"

    return [LINK_RE.sub(annotate, line) if ITEM_RE.match(line) else line for line in lines]


def write_report(path: Path, entries: list[Entry]) -> None:
    failed = [e for e in entries if e.status == FAIL]
    unsure = [e for e in entries if e.status == UNSURE]

    def table(rows: list[Entry]) -> list[str]:
        out = ["| Entry | Section | Reason |", "| --- | --- | --- |"]
        out += [f"| [{e.name}]({e.url}) | {e.section} | {'; '.join(e.reasons)} |" for e in rows]
        return out

    lines = [
        "# Entries hidden by the quality gate",
        "",
        "Generated daily by `scripts/build_readme.py`. These entries are in "
        "[list.md](list.md) but not shown in [README.md](README.md).",
        "",
        "Quality gate: GitHub repositories need at least "
        f"{MIN_STARS} stars, a commit within the last {MAX_INACTIVE_DAYS // 365} years and must not be "
        "archived. Other links must not be dead. An entry shows up again "
        "automatically as soon as it passes.",
        "",
        f"## Hidden ({len(failed)})",
        "",
        *(table(failed) if failed else ["None."]),
        "",
        f"## Could not be verified, still shown ({len(unsure)})",
        "",
        "These sites gave an ambiguous answer (often bot protection). They stay in the README.",
        "",
        *(table(unsure) if unsure else ["None."]),
        "",
    ]
    path.write_text("\n".join(lines))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", default=ROOT / "list.md", type=Path)
    ap.add_argument("--readme", default=ROOT / "README.md", type=Path)
    ap.add_argument("--report", default=ROOT / "excluded.md", type=Path)
    args = ap.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN is required", file=sys.stderr)
        return 2

    lines = args.source.read_text().splitlines(keepends=True)
    entries = parse_entries(lines)
    exceptions = load_exceptions()
    checked = [e for e in entries if e.url.rstrip("/") not in exceptions]

    gh_entries = [e for e in entries if github_repo(e.url)]
    keys = list_item_repo_keys(lines) | {repo_key(e.url) for e in gh_entries}
    info = fetch_github(sorted(keys), token)

    check_github([e for e in gh_entries if e in checked], info)
    check_links([e for e in checked if not github_repo(e.url)])

    drop = {e.line_no for e in entries if e.status == FAIL}
    args.readme.write_text("".join(add_stars(render(lines, drop), info)))
    write_report(args.report, entries)

    counts = {s: sum(e.status == s for e in entries) for s in (PASS, FAIL, UNSURE)}
    print(
        f"{len(entries)} entries: {counts[PASS]} passed, {counts[FAIL]} hidden, "
        f"{counts[UNSURE]} unverified (kept), {len(entries) - len(checked)} exempt"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
