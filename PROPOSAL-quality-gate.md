## Proposal: a quality gate for the README

Hi Peter,

the list has grown a lot, and a good part of it is abandoned by now. Reviewing every PR for "is this project any good?" doesn't scale either. So here's an idea that I've prototyped on the [`quality-gate`](https://github.com/awesome-mqtt/awesome-mqtt/tree/quality-gate) branch. Nothing on master is changed.

### How it works

- Contributors send PRs against **`list.md`** instead of `README.md`. We merge basically every reasonable PR there (format/lint still enforced).
- A **daily GitHub Action** generates `README.md` from `list.md` and leaves out entries that fail the gate:
  - GitHub repos: **≥ 10 stars**, **a commit within the last 2 years**, **not archived**
  - all links: **not dead** (404/410, unknown domain, refused connection, broken TLS). Ambiguous answers (403/429/timeouts, typically bot protection) do *not* remove an entry.
- Entries come back automatically once they pass again.
- `excluded.md` lists every hidden entry with its reason, so nobody has to wonder why their entry is missing.
- PRs get an informational (never failing) check: "your entry passes" / "will be hidden because …".
- `scripts/quality-gate-exceptions.txt` lets us exempt entries by hand.
- Bonus: every GitHub repo link in the README gets its current star count, e.g. **[Aedes](https://github.com/moscajs/aedes)** <small>★&nbsp;2k</small>. That's the same markup as on my profile page, refreshed daily.

Have a look at the result:
- Generated README: https://github.com/awesome-mqtt/awesome-mqtt/blob/quality-gate/README.md
- Hidden entries: https://github.com/awesome-mqtt/awesome-mqtt/blob/quality-gate/excluded.md
- Full diff: https://github.com/awesome-mqtt/awesome-mqtt/compare/master...quality-gate

### The catch: the numbers

With the rules as stated, **167 of 356 entries (47%) would be hidden** and 9 sections would vanish completely (all of Clojure, Dart, Delphi, GoLang, Objective-C, PHP, TCL, Telephony and Lighting).

| Rule set | Hidden |
| --- | --- |
| ≥10 stars + commit within 2 years (proposed) | 167 |
| ≥10 stars + commit within 3 years | 158 |
| ≥10 stars + commit within 5 years | 143 |
| ≥10 stars, no activity rule (archived still hidden) | 68 |
| any stars (0 is fine) + commit within 2 years | 140 |
| any stars (0 is fine) + commit within 3 years | 130 |
| any stars (0 is fine) + commit within 5 years | 115 |

(Not-found and archived repos are hidden in every variant.)

Almost all of the hiding comes from the activity rule: 99 entries fail *only* because of it, while dropping the star minimum saves just 27 entries. Among them are well-known projects like MQTT-Client-Framework (1.9k ★), esp_mqtt (1.2k ★), jeffallen/mqtt "MQTT for Go" (800+ ★), hbmqtt (800+ ★) and Mosquitto-PHP (500+ ★). Some of my own old mqtt-smarthome tools drop out too, and that's fine with me.

### Questions for you

1. **Activity rule**: keep 2 years as-is, or soften it? E.g. "active within 2 years **or** ≥ 100 stars", or only hide archived repos. My gut says the stars-OR-activity variant is the sweet spot, but I'd like your take.
2. **Commercial products**: do we want to list them at all? I think awesome lists are meant for awesome (open source) software, not for advertising. We could limit the list to open source projects (plus community resources like blogs and talks) and close vendor PRs right away.
3. **Non-GitHub entries** (~100: GitLab, app stores, blogs, project websites, commercial products) only get the dead-link check. OK for now, or should we add e.g. GitLab stars/activity?
4. **Exceptions**: OK to keep a manual exception list, and only for things both of us agree on?
5. **Bot commits to master**: the workflow pushes `README.md` as `github-actions[bot]`. That needs to be allowed if we turn on branch protection.
6. **Cleanup**: should entries that have been hidden for, say, a year get deleted from `list.md` eventually, or stay forever?

If you're on board in principle, I'd adjust the thresholds based on your answers and then open a PR.

---

_This file only exists on the proposal branch and will be removed before merging._
