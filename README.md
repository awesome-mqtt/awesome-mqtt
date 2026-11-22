# Awesome MQTT [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re) [![CC0](https://i.creativecommons.org/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

> A curated list of MQTT related stuff.

MQTT is a lightweight client-server publish/subscribe messaging protocol, optimized for high-latency or unreliable networks. This protocol is a good choice for Internet of Things applications, Telemetry, Sensor Networks, Smart Metering, Home Automation, Messaging and Notification Services.

## Contents

<!--lint disable double-link-->
- [Community Resources](#community-resources)
- [Brokers](#brokers)
- [Cloud](#cloud)
- [Platforms](#platforms)
- [Tools](#tools)
- [Clients](#clients)
- [Scripting](#scripting)
- [Interfaces](#interfaces)
    - [Makers](#makers)
    - [Industry](#industry)
    - [Operating System](#operating-system)
    - [Monitoring](#monitoring)
    - [Location Tracking](#location-tracking)
    - [Logging](#logging)
    - [Smart Home Hardware Interfaces](#smart-home-hardware-interfaces)
    - [Smart Home Integration Software](#smart-home-integration-software)
    - [Home Entertainment](#home-entertainment)
    - [Smart Metering](#smart-metering)
    - [Messaging](#messaging)
    - [Misc](#misc)
- [Visualization, Dashboards](#visualization-dashboards)
- [Architecture, Convention](#architecture-convention)
- [Security, Encryption](#security-encryption)
<!--lint enable double-link-->

### Contribute

Contributions welcome! Read the [contribution guidelines](contributing.md) first.

<!-- README.md is generated daily from list.md by scripts/build_readme.py. Please edit list.md, not README.md. -->

## Community Resources

- [mqtt.org](https://mqtt.org/)
- [MQTT community wiki](https://github.com/mqtt/mqtt.org/wiki)
- [Google Groups: MQTT](https://groups.google.com/g/mqtt)
- [IRC channel #mqtt on the freenode network](irc://irc.freenode.net/mqtt)
- [A list of public brokers](https://moxd.io/2015/10/17/public-mqtt-brokers/)

### Blogs

- [Ben Hardill](https://www.hardill.me.uk/wordpress/tag/mqtt/)
- [Jan-Piet Mens](https://jpmens.net/)
- [Nick O'Leary](https://knolleary.net/)
- [HiveMQ](https://www.hivemq.com/blog/)
- [EMQ](https://www.emqx.com/en/blog)
- [Amazon AWS IoT Blog](https://aws.amazon.com/blogs/iot/tag/mqtt/)

### Talks

- [An Introduction to MQTT: Why HTTP isn't the King of the Internet of Things](https://www.youtube.com/watch?v=LKz1jYngpcU) - Shinji Kim, Robert Bird - Akamai, Samsung Developer Conference 2017.
- [Einführung in MQTT](https://www.youtube.com/watch?v=INYG4-xsa9c) - Dominik Obermaier & Jens Deters, [Building IoT](https://www.buildingiot.de/index.php) conference 2016 (German).

## Brokers

- [Ably](https://www.ably.io/documentation/mqtt) - MQTT broker service and protocol adapter.
- [ActiveMQ](https://activemq.apache.org/) - A fast Java multiprotocol messaging and Integration Patterns server.
- [Aedes](https://github.com/moscajs/aedes) - Barebone MQTT broker that can run on any stream server, the node way.
- [Bevywise MQTTRoute](https://www.bevywise.com/mqtt-broker/) - MQTTRoute is an extendable & Scalable MQTT Broker with customizable UI, flexible storage & security options for all IoT / IIoT Implementation.
- [BifroMQ](https://bifromq.apache.org) - Java-based high-performance MQTT broker with native multi-tenancy for large-scale IoT.
- [comqtt](https://github.com/wind-c/comqtt) - A lightweight, high-performance go mqtt server(v3.0|v3.1.1|v5.0) supporting distributed cluster.
- [Eclipse Amlen](https://github.com/eclipse/amlen) - A scalable, secure, easy to use message broker that can be used for IoT, web and mobile use-cases. Open-sourced from IBM MessageSight.
- [Emitter](https://github.com/emitter-io/emitter) - A distributed, scalable and fault-tolerant publish-subscribe messaging platform based on MQTT protocol and featuring message storage.
- [EMQ X](https://github.com/emqx/emqx) - Scalable and Reliable Real-time MQTT Messaging Engine for IoT in 5G Era.
<!--lint disable double-link-->
<!--lint enable double-link-->
- [HiveMQ](https://www.hivemq.com/) - Java MQTT Broker that supports MQTT 3.1, 3.1.1 and 5.0. Commercial and open source editions available.
- [KMQTT](https://github.com/davidepianca98/KMQTT) - Kotlin Multiplatform MQTT broker, both embeddable and standalone.
- [Moquette](https://github.com/moquette-io/moquette) - Java MQTT lightweight broker.
- [Mosca](https://www.mosca.io/) - Node.js MQTT broker, which can be used Standalone or Embedded in another Node.js application.
- [Mosquitto](https://mosquitto.org/) - *"*The"** Open Source MQTT Broker.
<!--lint disable double-link-->
- [mqtt5](https://github.com/LabOverWire/mqtt-lib) - Async MQTT v5.0 broker in Rust with TCP, TLS, WebSocket, and QUIC transport, plus authentication, ACL, bridging, and session persistence.
<!--lint enable double-link-->
- [MyQttHub](https://myqtthub.com) - Cloud MQTT broker.
- [RabbitMQ](https://www.rabbitmq.com/mqtt.html) - High performance messaging broker with MQTT Adapter.
- [RobustMQ](http://robustmq.com) - Multi-protocol brokers written in Rust.
- [SurgeMQ](https://zhen.org/categories/surgemq/) - High Performance MQTT Server and Client Libraries in Go.
- [tbmq](https://github.com/thingsboard/tbmq) - Open-source, scalable, fault-tolerant and durable messaging broker for millions of IoT devices.
- [VelaMQ](https://www.velamq.com/) - Rust-based MQTT broker with clustering, a web console, authentication, topic ACLs, and a SQL rule engine.
- [VerneMQ](https://vernemq.com/) - Apache2 licensed distributed MQTT broker, developed in Erlang.
<!--lint disable double-link-->
- [Vert.x MQTT Server](https://github.com/vert-x3/vertx-mqtt) - Vert.x component to handle connections, communication and messages exchange with remote MQTT clients.
<!--lint enable double-link-->
- [Waterstream](https://waterstream.io/) - MQTT broker leveraging Apache Kafka as its own storage and distribution engine.
- [NanoMQ](https://github.com/nanomq/nanomq) - A light-weight and Blazing-fast MQTT Broker for IoT Edge platform.


## Cloud

- [Adafruit IO](https://io.adafruit.com) - Data-oriented IoT framework and libraries.
- [Alibaba Cloud IoT Platform](https://www.alibabacloud.com/product/iot) - Provides secure and reliable communication between devices and the IoT Platform which allows you to manage a large number of devices on a single IoT Platform.
- [AWS IoT Core](https://aws.amazon.com/iot-core/) - Managed cloud broker service supporting MQTT, MQTT over WSS, HTTPS and LoRaWAN.
- [Azure IoT Hub](https://azure.microsoft.com/en-us/services/iot-hub/) - Enable highly secure and reliable communication between your IoT application and the devices it manages. Azure IoT Hub provides a cloud-hosted solution backend to connect virtually any device. Extend your solution from the cloud to the edge with per-device authentication, built-in device management, and scaled provisioning.
- [CloudMQTT](https://www.cloudmqtt.com/) - Hosted message broker for the Internet of Things. Perfectly configured and optimized message queues for IoT, ready in seconds.
- [CloudAMQP](https://www.cloudamqp.com/docs/mqtt.html) - Hosted AMQP brokers with MQTT support.
- [ConnectMQ](https://connectmq.com/) - Managed MQTT broker with MQTT 3.1.1 and 5.0, TLS, WebSockets and per-topic access control, no servers to run.
- [CrystalMQ](https://www.bevywise.com/hosted-mqtt-server/) - Fully Managed Cloud MQTT Broker for large scale deployments.
- [flespi](https://flespi.com/mqtt-broker) - Free and secure cloud MQTT broker with private namespaces, MQTT 3.1.1 and MQTT 5.0 support and gorgeous limits.
- [Google Cloud IoT](https://cloud.google.com/solutions/iot/) - Cloud managed MQTT service.
- [HiveMQ Cloud](https://www.hivemq.com/cloud/) - Cloud managed MQȚT service.

## Platforms

- [AyMON](https://www.aymon.ca) - Industrial monitoring and automation engine with a built-in MQTT 3.1.1 / 5 broker and client: Modbus, OPC UA, SNMP and SQL devices in one live tree with alarms, history, web pages and clustering, configured in XML. A free edition and runnable examples are on [GitHub](https://github.com/akya-dev/AyMON).
- [DeviceChain](https://devicechain.io) - Apache-2.0, multi-tenant IoT platform for Kubernetes with a built-in MQTT 3.1.1 broker (TLS, QoS 0/1, per-device credentials or client certificates), plus Sparkplug B, LwM2M and HTTP ingest, rules, alarms, commands and dashboards.
- [Iotellect](https://iotellect.com/) - Low-code IoT/IIoT platform for industrial automation, SCADA, BMS and remote monitoring. Supports MQTT, OPC-UA, Modbus and 100+ protocols with visual development tools and edge-cloud integration.
- [mainflux](https://www.mainflux.com/) - Device management, data aggregation, data management, data analytics,connectivity and message routing and event management. Supported by Linux Software Foundation.
- [thingsboard](https://thingsboard.io/) - Device management, data collection, processing, event management, and visualization for your IoT projects.
- [ForestHub](https://foresthub.ai) - Edge AI agent platform; its open-source runtime [edge-agents](https://github.com/ForestHubAI/edge-agents) orchestrates AI agents on Linux edge gateways with MQTT as a first-class workflow transport, running offline with local SLMs alongside cloud LLMs.
- [IoT DC3](https://github.com/pnoker/iot-dc3) - Fully open-source, distributed industrial IoT platform built on Spring Cloud, with 28 built-in protocol drivers (including MQTT), AI-powered operations via Spring AI, and microservice architecture. ([Docs](https://docs.dc3.site))


## Tools
- [Cortex](https://github.com/cortex-docs/cortex) - Generates interactive documentation, typed SDKs, and MCP servers from AsyncAPI definitions, including MQTT APIs.
- [IoT-Testware](https://projects.eclipse.org/projects/technology.iottestware) - The Eclipse IoT-Testware is a collection of conformance test suites for IoT protocols enriched with additional tools for fuzzing and performance testing.
- [Katman MQTT](https://www.katmanmqtt.com/) - MQTT client for Windows and Linux with reusable publish templates, selected-topic logging, and request/response debugging tools.
- [LabOverWire](https://laboverwire.com/features) - Visual diagram editor for designing MQTT topologies, built with Rust (WebAssembly) and TypeScript. Features live in-browser simulation, code generation, and AsyncAPI export.
- [LazyMQTT](https://github.com/ScottFelder/lazymqtt) - A fast, terminal-UI MQTT client written in Rust — inspired by MQTT Explorer, but keyboard-driven and living in your terminal.
- [LibreDB Studio](https://github.com/libredb/libredb-studio) - Open source web database IDE with a read-only MQTT 5.0 connection: browse a broker's live topic tree with retained messages and read topics, including Sparkplug B payloads.
- [Mer-cli](https://github.com/iotmertech/iot-data-generator) - A high-performance IoT data generator written in Rust. Supports MQTT, HTTP, and TCP for simulating realistic sensor payloads with Handlebars templates.
- [mockd](https://github.com/getmockd/mockd) - Multi-protocol mock server with a built-in MQTT broker supporting QoS 0-2, retained messages, topic patterns, and device simulation for IoT development and testing.
- [MockForge](https://github.com/SaaSy-Solutions/mockforge) - Open-source multi-protocol mock server written in Rust with a built-in MQTT 3.1.1/5.0 broker for testing, alongside HTTP, gRPC, GraphQL, WebSocket, Kafka and AMQP mocks.
- [MQTT Board](https://github.com/flespi-software/MQTT-Board) - Open-source diagnostic-oriented MQTT client tool.
- [MQTT Commander for iOS](https://mqttcommander.com) - Native iPhone and iPad client with a live topic tree, topic board, JSON inspection, and a 13-stage Connection Doctor. Supports MQTT 3.1.1 and 5.0 over TCP, TLS, mTLS and WebSocket.
- [MQTT CLI](https://github.com/hivemq/mqtt-cli) - A command line interface for connecting various MQTT clients supporting MQTT 5.0 and 3.1.1.
- [mqtt-client](https://github.com/sdeancos/mqtt-client) - Simple MQTT Client command line (Python) (use paho lib).
- [mqtt-mirror](https://github.com/4nte/mqtt-mirror) - Mirror MQTT traffic from one broker to another. Available as a CLI tool, Helm chart or Docker image.
- [mqtt_recorder](https://github.com/rpdswtk/mqtt_recorder) - Simple cli tool for recording and replaying MQTT messages.
- [mqtt-spy](https://kamilfb.github.io/mqtt-spy/) - Java based MQTT frontend. Supports scripting.
- [mqtt-studio](https://www.mqttstudio.com) - A practical MQTT Tool with an innovative UI, designed for developers to efficiently create, test, and manage MQTT-based applications, enhancing their development and support workflows.
- [MQTT.fx](https://mqttfx.jensd.de/) - MQTT Client written in Java based on Eclipse Paho. Supports scripting.
- [Mqttable](https://mqttable.com/) - A desktop MQTT workbench for traffic inspection, replay, load testing, fault injection, and PCAP analysis.
- [MQTTLens](https://chrome.google.com/webstore/detail/mqttlens/hemojaaeigabkbcookmlgmdigohjobjm) - A Google Chrome application, which connects to a MQTT broker and is able to subscribe and publish to MQTT topics.
- [MQTT Explorer](https://mqtt-explorer.com/) - Tool to visualize your MQTT topics in a topic hierarchy, a MQTT swiss-army knife.
- [MQTT TUI](https://github.com/EdJoPaTo/mqttui) - Simple lightweight terminal based MQTT monitor and publisher.
- [MQTTProbe](https://github.com/bluegrassiot/mqttprobe) - Cross platform MQTT diagnostic client for IIoT with live topic browsing, payload decoding across multiple formats, charting, built in emulators, and advanced Sparkplug B integration.
- [RunMQTT MQTT Topic ACL Linter](https://runmqtt.com/mqtt-acl-linter) - Browser-based, local-only validator for MQTT topic-filter ACLs that checks wildcard breadth, tenant boundaries, publish/subscribe direction, placeholders, and overlapping rules. [Source and method](https://github.com/visoar/mqtt-acl-linter).
- [SimpleMQTT](https://simplemqtt.theoi.de/) - A Slack app to send messages from Slack to MQTT brokers with slash commands.
- [Spitfire](https://usespitfire.com/guides/mqtt-load-testing) - Self-hosted distributed load testing platform with a web UI; simulates thousands of MQTT devices (QoS 0/1/2 publish, subscribe, request-reply) alongside HTTP, Kafka and other protocols. Commercial, with a free edition.
- [TopicBench](https://github.com/unipsycho/topicbench) - Free open-source multi-broker MQTT explorer and monitor desktop client, written in Rust.
- [VSMQTT](https://github.com/rpdswtk/vsmqtt) - Simple MQTT client integrated in Visual Studio Code.
- [MQTTX](https://github.com/emqx/MQTTX) - Cross-platform MQTT desktop client open sourced by EMQ, which supports macOS, Linux, and Windows.
- [MIMIC MQTT Simulator](https://www.gambitcomm.com/site/mqttsimulator.php) - Simulate up to 100,000 MQTT clients per server for development/testing/deployment of IoT applications.
- [mqtt-stats](https://github.com/gambitcomminc/mqtt-stats) - Subscriber client to monitor MQTT Topic Statistics.
<!--lint disable double-link-->
- [mqttv5](https://github.com/LabOverWire/mqtt-lib) - Unified MQTT v5.0 CLI for publishing, subscribing, running a broker, and benchmarking with multi-transport support.
<!--lint enable double-link-->

## Clients


### Multi-Platform

- [Paho](https://www.eclipse.org/paho/) - Open source client implementations for C,C++, Java, Python, JavaScript, GoLang, C#, Rust, Android and Embedded (Arduino/mbed).
- [mosquitto-clients](https://mosquitto.org/download/) - [mosquitto_pub](https://mosquitto.org/man/mosquitto_pub-1.html) and [mosquitto_sub](https://mosquitto.org/man/mosquitto_sub-1.html) CLI clients for most operating systems and [libmosquitto](https://mosquitto.org/man/libmosquitto-3.html) for integration.
- [TestMQTT](https://testmqtt.com/) - Free browser-based MQTT client for testing any broker over WebSockets: connect, subscribe, publish and debug topics with no install or sign-up.

### Python

- [aiomqtt](https://github.com/empicano/aiomqtt) - The idiomatic asyncio MQTT client.
- [gmqtt](https://github.com/wialon/gmqtt) - Python MQTT v5.0 client (asyncio-based).
<!--lint disable double-link-->
<!--lint enable double-link-->
- [MiniMQTT](https://github.com/adafruit/Adafruit_CircuitPython_MiniMQTT) - MQTT Client Library for CircuitPython.

### JavaScript

- [MQTT.js](https://github.com/mqttjs) - MQTT client for Node.js.
- [mqtt-wrapper](https://www.webcomponents.org/element/hobbyquaker/mqtt-wrapper/elements/mqtt-wrapper) - Polymer Element that wraps other Elements and links them to MQTT topics.
<!--lint disable double-link-->
- [Vert.x Client](https://github.com/vert-x3/vertx-mqtt) - Vert.x component that provides methods for connecting/disconnecting to a broker, publishing messages and subscribing to topics.
<!--lint enable double-link-->

### Java

- [hivemq-mqtt-client](https://github.com/hivemq/hivemq-mqtt-client) - High-performance Java MQTT client library with different API flavours for MQTT 5.0 and 3.1.1.

### Erlang or Elixir

- [emqttc](https://github.com/emqx/emqtt) - Asynchronous Erlang MQTT Client.

### Ballerina

- [ballerina-mqtt](https://github.com/ballerina-platform/module-ballerina-mqtt) - Ballerina MQTT client based on paho-mqtt.

### C or C++

- [mqtt_cpp](https://github.com/redboltz/mqtt_cpp) - MQTT client for C++14 based on Boost.Asio.
- [MQTT-C](https://github.com/LiamBindle/MQTT-C) - A portable MQTT C client for embedded systems and PCs alike.
- [wolfMQTT](https://www.wolfssl.com/products/wolfmqtt/) - A client implementation of the MQTT written in C for embedded use. It supports SSL/TLS via the wolfSSL library.

### C# / .NET

- [HiveMQtt](https://github.com/hivemq/hivemq-mqtt-client-dotnet) - MQTT 5.0 compliant secure client with automatic back pressure management and TCP & WebSocket transport support.
- [MQTTnet](https://github.com/chkr1011/MQTTnet) - MQTT client and broker .NET implementations.

### Lua

- [luamqtt](https://github.com/xHasKx/luamqtt/) - Pure-lua MQTT v3.1.1 and v5.0 client.
- [mqtt_lua](https://geekscape.github.io/mqtt_lua/) - MQTT Client library for the Lua language.

### Ruby

- [ruby-mqtt](https://github.com/njh/ruby-mqtt) - Pure Ruby gem that implements the MQTT protocol.

### Rust

- [AimDB](https://github.com/aimdb-dev/aimdb) - Typed, versioned data contracts over MQTT from `no_std` microcontrollers (Embassy) to the cloud (Tokio), with schema migrations at the hub.
- [mqtt-typed-client](https://github.com/holovskyi/mqtt-typed-client) - Type-safe async MQTT client built on rumqttc, with derive macros for typed topics, automatic (de)serialization, and tree-based message routing.
<!--lint disable double-link-->
- [mqtt5](https://github.com/LabOverWire/mqtt-lib) - Complete async MQTT v5.0 client and broker library for Rust with TCP, TLS, WebSocket, and QUIC support.
<!--lint enable double-link-->

### Swift

- [CocoaMQTT](https://github.com/emqx/CocoaMQTT) - MQTT for iOS and macOS written with Swift.
- [Moscapsule](https://github.com/flightonary/Moscapsule) - MQTT Client for iOS written in Swift.

## Scripting

- [Node-RED](https://nodered.org/) - A visual tool for wiring the Internet of Things.

## Interfaces

### Makers

- [MySensors](https://www.mysensors.org/) - Arduino NRF24L01 based sensor network with support for an MQTT gateway.

#### ESP
- [pubsubclient](https://github.com/knolleary/pubsubclient) - A client library for the Arduino Ethernet Shield that provides support for MQTT.
- [ESP32-BLE2MQTT](https://github.com/shmuelzon/esp32-ble2mqtt) - BLE to MQTT bridge, exposes BLE GATT characteristics as MQTT topics for bidirectional communication.
- [ESP8266MQTTMesh](https://github.com/PhracturedBlue/ESP8266MQTTMesh) - MQTT over mesh WiFi integrated library for ESP8266.
- [mqtt-with-micropython](https://docs.pycom.io/tutorials/networkprotocols/mqtt/) - Connect to MQTT with micropython and wipy/others (ESP32 inside).


#### Firmwares for ESP based Devices

There are many inexpensive smart home Wi-Fi devices based on inexpensive ESP8266 chip *(see: [1](https://templates.blakadder.com/index.html), [2](https://github.com/xoseperez/espurna/wiki/Hardware), [3](https://www.letscontrolit.com/wiki/index.php?title=ESP_Hardware))*. Most of them can be reflashed with custom firmware.
Here are complete firmwares to turn them into MQTT-controlled smart home nodes:

- [ESPEasy](https://www.letscontrolit.com/wiki/index.php?title=ESPEasy) - Turns ESP into a multifunction sensor device for <abbr title="Home automation">HA</abbr> solutions with web-based configuration.
- [ESPHome](https://esphome.io/) - Builds ESP8266/ESP32 firmware from concise YAML descriptions, uploads to and manages flashed devices.
- [Espurna](https://github.com/xoseperez/espurna) - <abbr title="Home automation">HA</abbr> firmware for ESP8266-based devices with rich web UI and ≈120 devices supported out of the box.
<!--lint disable double-link-->
- [HomeGenie Mini](https://homegenie.it/) - Smart device firmware for ESP8266/ESP32 supporting remote monitoring and controlling via MQTT with end-to-end encryption. The firmware is open source and it can be uploaded to the ESP device directly from the website.
<!--lint enable double-link-->
- [OpenMQTTGateway](https://github.com/1technophile/OpenMQTTGateway) - MQTT gateway for ESP8266, ESP32, Sonoff RF Bridge or Arduino with bidirectional 433mhz/315mhz/868mhz, Infrared communications, BLE, beacons detection, mi flora, mi jia, LYWSD02, LYWSD03MMC, Mi Scale compatibility, SMS & LORA.
- [Sonoff-Tasmota](https://github.com/arendst/Tasmota) - Firmware for ESP8266 devices with web-based configuration. ≈500 devices supported (not only Sonoffs).
- [WiFi-IoT](https://wifi-iot.com/p/wiki/) - ESP8266/ESP32 firmware builder. Partly in Russian. Free features are limited.


### Industry

- [spicierModbus2mqtt](https://github.com/mbs38/spicierModbus2mqtt) - Modbus master which publishes register values via MQTT.
- [OPC Router](https://www.opc-router.com/4_1-mqtt-client-opc-router-plug-in-en/) - MQTT Gateway (publisher/subscriber) with various plug-ins (OPC UA Bridge, SQL Bridge, REST Bridge, SAP Bridge).


### Operating System

- [updates2mqtt](https://updates2mqtt.rhizomatics.org.uk) - Check for Docker image updates and publish to MQTT, in structure to support Home Assistant's automated Updates and Discovery.
- [psmqtt](https://github.com/eschava/psmqtt) - Utility reporting system health and status via MQTT.


### Monitoring

- [mqttwarn](https://mqttwarn.readthedocs.io/) - Route and transform MQTT notifications, with 70+ built-in adapters for databases, messaging and other notification sinks.
- [snmp2mqtt](https://c0d3.sh/andre/snmp2mqtt) - Python based SNMP v2 and v3 bridge to MQTT, active project in late 2025.
- [SolidPing](https://github.com/fclairamb/solidping) - Uptime monitoring with an MQTT broker check that connects (optional TLS and auth), publishes a message on a topic and waits for it to come back, recording connect and round-trip times. Also HTTP, TCP, DNS and many other check types, self-hosted or hosted.
- [check-mqtt](https://github.com/jpmens/check-mqtt) - A Nagios/Icinga plugin for checking connectivity to an MQTT broker.


### Location Tracking

- [ADSBiq](https://adsbiq.com/api/other/mqtt) - Authenticated retained-delta aircraft state over MQTT WebSockets for bounded IoT and location-aware integrations.
- [OwnTracks](https://owntracks.org/) - Location tracking and geofencing for MQTT.

### Logging

- [influx4mqtt](https://github.com/hobbyquaker/influx4mqtt) - Subscribe to MQTT topics and insert into InfluxDB.
<!--lint disable double-link-->
- [mqttwarn](https://github.com/jpmens/mqttwarn) - Use with [carbon](https://mqttwarn.readthedocs.io/notifier-catalog.html#carbon) plugin.
<!--lint enable double-link-->


### Smart Home Hardware Interfaces

- [airrohr2mqtt](https://c0d3.sh/smarthome/airrohr2mqtt) - Air quality monitoring integration.
- [ble-scale-sync](https://github.com/KristianP26/ble-scale-sync) - BLE-to-MQTT bridge for smart scales (23 brands) with Home Assistant auto-discovery. Reads weight + impedance, calculates body composition, publishes all 11 metrics with LWT and display precision. [Website](https://blescalesync.dev).
- [Bambuddy](https://github.com/maziggy/bambuddy) - Self-hosted management tool for Bambu Lab 3D printers using MQTT, with real-time monitoring, scheduling, and Home Assistant integration.
- [coe2mqtt](https://c0d3.sh/smarthome/coe2mqtt) - Bi-directional CAN Bus to MQTT.
- [fronius2mqtt](https://c0d3.sh/smarthome/fronius2mqtt) - MQTT integration for Fronius SolarAPI.
- [hm2mqtt.js](https://github.com/hobbyquaker/hm2mqtt.js) - Interface between EQ-3's Homematic line of smarthome devices and MQTT. Supports Homematic IP.
- [huABus](https://github.com/arboeh/huABus) - Home Assistant application (Add-on) and MQTT bridge for Huawei solar inverters (SUN2000/3000/5000).
- [knx-mqtt-bridge](https://github.com/pakerfeldt/knx-mqtt-bridge) - Bridges KNX and MQTT using the knx.js library.
- [mcsMQTT](https://shop.homeseer.com/products/mcsmqtt-software-plug-in-for-hs3) - Plug-in for HS3 (HomeSeer).
<!--lint disable double-link-->
<!--lint enable double-link-->
- [zigbee2mqtt](https://github.com/Koenkk/zigbee2mqtt) - Allows you to use your Zigbee devices without the vendors (Xiaomi/TRADFRI/Hue) bridge/gateway.
- [zwavejs2mqtt](https://github.com/zwave-js/zwavejs2mqtt) - Zwave to Mqtt gateway and Control Panel Web UI.


### Smart Home Integration Software

- [Home Assistant](https://www.home-assistant.io) - Home Automation system with native MQTT support, and the world's largest non-commercial Open Source project.
- [Domoticz](https://www.domoticz.com/) - Home Automation system with MQTT support.
- [FHEM](https://fhem.de/fhem.html) - Includes a [MQTT module](https://fhem.de/commandref.html#MQTT) since V5.6.
- [Homegear](https://homegear.eu/index.php/Main_Page) - Built in MQTT support.
<!--lint disable double-link-->
- [HomeGenie](https://homegenie.it/) - Supports remote controlling and monitoring via MQTT with end-to-end encryption.
<!--lint enable double-link-->
- [ioBroker](https://github.com/ioBroker) - Includes a [MQTT adapter](https://github.com/ioBroker/ioBroker.mqtt).
- [openHAB](https://github.com/openhab) - Includes a [MQTT binding](https://github.com/openhab/openhab1-addons/wiki/MQTT-Binding).
- [openLuup](https://github.com/akbooer/openLuup) - A pure-Lua open-source emulation of the Vera Luup home automation environment with MQTT.
- [pimatic](https://pimatic.org/) - MQTT plugin included.
- [she - smart home engine](https://github.com/hobbyquaker/she) - Scriptable smart home automation engine with AI assistance.
- [knx2mqtt](https://c0d3.sh/smarthome/knx2mqtt) - Telegram bi-directional integration as alternative to HomeAssistant's built-in support.


### Home Entertainment

- [chromecast-mqtt-connector](https://github.com/nohum/chromecast-mqtt-connector) - Control your Google Chromecast devices using MQTT.
- [lgtv2mqtt](https://github.com/hobbyquaker/lgtv2mqtt) - Interface between LG WebOS Smart TVs and MQTT.
- [sonos2mqtt](https://github.com/svrooij/sonos2mqtt) - A bridge between Sonos and MQTT.
- [VLC MQTT Module](https://wiki.videolan.org/Documentation:Modules/mqtt/) - Control VLC via MQTT.


### Smart Metering

- [rpi-mqtt-monitor](https://github.com/hjelev/rpi-mqtt-monitor) - The easiest way to track your Raspberry Pi or Ubuntu computer system health and performance in Home Assistant via MQTT.


### Messaging

<!--lint disable double-link-->
- [mqttwarn](https://github.com/jpmens/mqttwarn) - Subscribe to MQTT topics (with wildcards) and notify pluggable services.
<!--lint enable double-link-->


### Misc

- [anpr2mqtt](https://anpr2mqtt.rhizomatics.org.uk) - Listen for images on file server, analyze and create Home Assistant entities via MQTT Discovery.
- [chrome2mqtt](https://github.com/tbowmo/chrome2mqtt) - Python program to enable MQTT control endpoints for chromecasts (both audio and video).
- [MQTT.Cool](https://mqtt.cool) - A web gateway that optimizes any MQTT broker when sending real-time data to web clients with automatic throttling.
- [mqtt-camera-streamer](https://github.com/robmarkcole/mqtt-camera-streamer) - Stream images from a connected camera over MQTT & view using Streamlit.
- [mqtt-transformer](https://github.com/tg44/mqtt-transformer) - A simple service which consumes, transforms and periodically republish json messages on MQTT.
- [serial2mqtt](https://github.com/vortex314/serial2mqtt) - A Linux gateway to connect low-cost microcontrollers only with a serial port to MQTT.
- [speedtest2mqtt](https://github.com/hobbyquaker/speedtest2mqtt) - Run speedtest-cli and publish results via MQTT.
- [unifi2mqtt](https://github.com/hobbyquaker/unifi2mqtt) - Publish connected clients from Ubiquiti Unifi to MQTT.
- [Valetudo](https://github.com/Hypfer/Valetudo) - Xiaomi (Roborock) Vacuum Robots Firmware with MQTT and Webinterface.
- [wlan-thermo-mqtt-addon](https://bitbucket.org/IOcastor/wlan-thermo-mqtt-addon/) - Addon for a popular DIY barbecue thermometer.


## Visualization, Dashboards

- [Feezal](https://github.com/feezal/feezal) - Dashboard editor powered by Web Components and MQTT.
- [mqtt-dashboard](https://github.com/jmischler72/mqtt-dashboard) - Self-hostable MQTT dashboard/explorer with drag-and-drop panels like cron, button, log and topic browser to help interact and monitor MQTT topics.
- [MQTT Dash](https://play.google.com/store/apps/details?id=net.routix.mqttdash&hl=de) - Android App: With the app you can create dashboards for your MQTT enabled IoT Smart Home devices and applications.
- [MQTT.Cool Test Client](https://testclient-cloud.mqtt.cool) - A web interface for testing interaction between MQTT.Cool and any MQTT broker.
- [mqtt-panel](https://github.com/fabaff/mqtt-panel) - A web interface for MQTT.
- [MQTT-Tiles](https://github.com/flespi-software/MQTT-Tiles) - MQTT-based IoT dashboard visualization tool. Allows easy dashboards sharing. Works with any MQTT broker supporting the WSS protocol.
- [MYHELLOIOT](https://adrianromero.github.io/myhelloiot/) - MQTT dashboard application.
- [node-red-dashboard](https://github.com/node-red/node-red-dashboard) - A dashboard UI for Node-RED.
- [PlotJuggler](https://github.com/facontidavide/PlotJuggler) - Visualize time series (from sources such as: MQTT, Websockets, ZeroMQ, UDP, etc., supports data formats such as JSON, CBOR, BSON, Message Pack, etc.). It is a fast, powerful and intuitive cross-platform tool.
- [ZigDash](https://gitlab.com/tamamg/zigdash) - Free, open-source Material 3 MQTT dashboard for Android, built for Zigbee2MQTT with automatic device discovery. Also on [Google Play](https://play.google.com/store/apps/details?id=com.giladtamam.zigdash).

<!--lint disable double-link-->
Other tools that can be used to create Visualization/Dashboards can be found under [Platforms](#platforms) and [Smart Home Integration Software](#smart-home-integration-software).
<!--lint enable double-link-->

## Architecture, Convention

- [mqtt-smarthome](https://github.com/mqtt-smarthome/mqtt-smarthome) - Smart home automation with MQTT as the central message bus - Architectural proposal.
- [The Homie Convention](https://github.com/homieiot/convention) - A lightweight MQTT convention for the IoT.

## Security, Encryption

- [Let's Encrypt Mosquitto Docker Container](https://hub.docker.com/r/pythonlinks/letsencrypt-mosquitto) - Easier TLS certificate management for brokers.
- [Teserakt E4](https://teserakt.io/) - End-to-end encryption and key management for MQTT and other M2M protocols – Open-source and paid plans.
