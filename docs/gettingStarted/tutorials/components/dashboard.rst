RoboSAPIENS Dashboard (Dash + Redis) — Tutorial
================================================

**Repository:** `link <https://github.com/saharnn96/robosapiens-dashboard>`_

Overview
--------
This tutorial explains how the real-time dashboard in ``app.py`` works:
- Visualizes recent execution windows for device components.
- Shows device online/offline status and component controls.
- Streams logs from Redis lists, with selectable sources.
- Displays trustworthiness events from a Redis pub/sub topic as a toast and timeline spikes.

Architecture
------------
- Dash single-page app with periodic callbacks.
- Redis for key-value, lists, and pub/sub:
  - Device registry and heartbeats
  - Component status and execution history
  - Centralized logging (lists ending with ``:logs``)
  - Trustworthiness pub/sub (topic: ``maple``)

Prerequisites
-------------
- Python 3.9+
- Redis 7+
- Dependencies: ``pip install -r requirements.txt``

Quick Start
-----------
Local:
- Start Redis and run: ``python app.py``
- Visit: http://localhost:8050
- Optional: populate fake data: ``python redis_filler.py``

Docker:
- ``docker compose up --build`` (serves Dash on 8050, Redis on 6379)

Configuration (env)
-------------------
- ``REDIS_HOST`` (default: ``localhost``)
- ``REDIS_PORT`` (default: ``6379``)
- ``REDIS_DB`` (default: ``0``)
- ``DASH_HOST`` (default: ``0.0.0.0``)
- ``DASH_PORT`` (default: ``8050``)
- ``TRUST_DISPLAY_SECONDS`` (default: ``5``)

Redis Data Model
----------------
Device registry:
- ``devices:list`` — list of device names
- ``devices:{device}:heartbeat`` — UNIX ts of last heartbeat
- ``devices:{device}:nodes`` — list of node names

Component state and execution:
- ``devices:{device}:{node}:status`` — "running"|"paused"|"stopped"|"exited"|...
- ``devices:{device}:{node}:execution_history`` — LIFO list of ``start_ts,duration,status``
- Optional live fields consumed into history:
  - ``{node}:execution_time`` or ``devices:{device}:{node}:execution_time``
  - ``{node}:start_execution`` or ``devices:{device}:{node}:start_execution``

Logging:
- Any key that ends with ``:logs`` is treated as a source.
- The dashboard also writes to ``dashboard:logs``.

Trust:
- Pub/sub topic ``maple`` with JSON or string payload that resolves to bool.
  - Examples: ``{"Bool": true}``, ``{"trust": "false"}``, ``"true"``

UI Walkthrough
--------------
Header
- Title and brief description.

Components Timeline
- Horizontal bars show recent execution windows (last 15s).
- Color scheme per phase name (e.g., Monitor/Analysis/Plan/... if component names match).
- A "🛡️ Trustworthiness" row shows short spikes for trust events (green for OK, red for ALERT).
- Vertical "Now" dashed line at t=0.

Device Status
- One card per device with:
  - Online/Offline based on heartbeat (10s threshold).
  - Active count (running components).
  - Component list with status and action buttons:
    - ▶️ Run publishes ``{"command":"up","app":node}`` to ``{device}-orchestrator``
    - ⏸️ Pause publishes ``{"command":"down","app":node}`` to ``{device}-orchestrator``
  - Buttons show a temporary loading state until Redis status reflects the change (or timeout).

System Logs
- Checklist auto-discovers keys ending with ``:logs`` (plus ``log`` if present).
- Shows merged tail (last 10 entries) for selected sources, prefixed with source name.

How It Works (Key Parts)
------------------------
Logging to Redis
- ``RedisLogHandler`` pushes formatted log lines to ``dashboard:logs`` and trims to max size.

Trust Listener Thread
- Background thread subscribes to ``maple``.
- Parses payloads into True/False and updates:
  - In-memory state for the toast (auto-hides after ``TRUST_DISPLAY_SECONDS``).
  - Short in-memory history for plotting spikes on the timeline.

Gantt Update
- Callback: ``update_gantt`` every 1s.
- Reads devices and nodes, collects recent execution windows from:
  1) Per-node execution_history (filtered to recent "running" entries)
  2) Live execution_time/start_execution (de-duplicated, then stored into history)
- Adds trust spikes if events occurred within the time window.

Devices and Actions
- Callback: ``update_processors`` every 2s.
- Computes per-device status from heartbeat.
- Enforces "stopped" state for nodes if device is offline.
- Renders per-node controls with loading-state management.

Actions Publishing
- Callback: ``handle_actions`` receives clicks and publishes to ``{device}-orchestrator`` channels:
  - Run => ``{"command":"up","app":node}``
  - Pause => ``{"command":"down","app":node}``
- Uses a small in-memory map to show loading; clears once Redis status flips or times out.

Log Sources and Stream
- ``update_log_sources`` and ``auto_refresh_log_sources`` scan for ``*:logs`` keys.
- ``update_log`` renders the tail of selected sources, prefixed with source names.

Developing and Testing
----------------------
Populate demo data
- Use the included generator:
  - ``python redis_filler.py``

Common Checks
- No devices/cards: ensure ``devices:list`` exists with device names.
- No timeline bars: ensure nodes have execution_time/start_execution and status=running.
- No logs: ensure at least one ``*:logs`` list exists with entries.
- No trust toast/spikes: publish on ``maple``, e.g.:
  - ``PUBLISH maple '{"Bool": true}'``

Extending
---------
- Add new phases by extending the color map in the timeline callback.
- Persist longer execution history by increasing Redis list trims.
- Wire additional actions (build/remove) by publishing new commands to orchestrators.
- Adjust heartbeat thresholds and time windows for your system scale.

Security and Ops
----------------
- Docker image runs as non-root (``dashuser``).
- Health check polls ``/`` on port 8050.
- Redis persistence is enabled in ``docker-compose.yml`` via ``appendonly yes``.
