Trustworthiness Checker - Tutorial
=================================
**Repository:** `link <https://github.com/INTO-CPS-Association/robosapiens-trustworthiness-checker>`_


This tutorial walks you through building, configuring, and running the
Trustworthiness Checker from this repository. You will learn how to
use file traces, MQTT, Redis, and ROS 2 as I/O backends, and how to
try distributed execution modes and the work scheduler.

Prerequisites
-------------

- Rust toolchain (Rust 1.85+ recommended) with Cargo
- Optional backends depending on what you want to try:

  - MQTT broker (e.g., EMQX, Mosquitto). A ready-to-use EMQX service is
    provided via ``docker/docker-compose.yaml``.
  - Redis server (only if trying Redis I/O)
  - ROS 2 Humble (only if trying ROS I/O). The Dockerfile targets Humble.

- Python is not required for the core tool, but some scripts under
  ``scripts/`` may use it.

Build from source
-----------------

1. Clone this repository and change into it.
2. Build in debug or release mode:

   - Debug (faster builds)::

       cargo build

   - Release (faster runtime)::

       cargo build --release

Set logging verbosity (optional) by setting ``RUST_LOG`` before running,
for example ``info`` or ``debug``. In PowerShell::

   $env:RUST_LOG = "info"

A quick look at the CLI
-----------------------

The executable is the default run target for the crate and supports
multiple I/O backends and distribution modes. Common flags:

- Model/specification file: ``<path-to-model.lola>`` (first positional)
- Input (choose one):

  - ``--input-file <path>``
  - ``--input-mqtt-topics <t1> <t2> ...`` or ``--mqtt-input``
  - ``--input-redis-topics <t1> <t2> ...`` or ``--redis-input``
  - ``--input-ros-topics <ros_mapping.json>`` (ROS 2 feature)
  - ``--input-map-mqtt-topics <t1> <t2> ...`` (structured/generic MQTT input)

- Output (choose one):

  - ``--output-stdout``
  - ``--output-mqtt-topics <t1> <t2> ...`` or ``--mqtt-output``
  - ``--output-redis-topics <t1> <t2> ...`` or ``--redis-output``
  - ``--output-ros-topics ...`` (not implemented yet)

- Distribution (optional): see the section "Distributed execution" below.
- Ports (optional): ``--mqtt-port <u16>``, ``--redis-port <u16>``
- Parser/language (optional): ``--parser-mode combinator|lalr``,
  ``--language dynsrv|lola`` (LOLA is an alias for DynSRV).

Data format
-----------

Values are exchanged as JSON. For integer values, wrap in a variant object::

  { "Int": 42 }

To send an unknown value, use::

  { "Unknown": null }

The tool also supports richer types in examples that use lists and
records (see ``examples/distributed/mqtt_dist_echo.lola``).

Quick start: file input and stdout output
----------------------------------------

Use the minimal example in ``examples/simple_add.lola`` and a matching
trace in ``examples/simple_add.input``.

- Model (``examples/simple_add.lola``)::

    in x
    in y
    out z
    z = x + y

- Trace (``examples/simple_add.input``)::

    0: x = 1
       y = 2
    1: x = 3
       y = 4

Run the monitor and print results to stdout::

  cargo run -- examples/simple_add.lola --input-file examples/simple_add.input --output-stdout

MQTT I/O
--------

A working MQTT broker is required. You can use the EMQX service defined
in ``docker/docker-compose.yaml``.

Publish/subscribe topics are bound by name to stream variables when you
use ``--input-mqtt-topics`` and ``--output-mqtt-topics``.

Example: add two inputs and publish the result on topic ``z``::

  cargo run -- examples/simple_add.lola --input-mqtt-topics x y --output-mqtt-topics z

Then publish two messages (e.g., with MQTT Explorer) to topics ``x`` and
``y`` respectively::

  { "Int": 42 }

You should see the output on topic ``z``::

  { "Int": 84 }

Notes
^^^^^

- If your specification declares auxiliary streams, current MQTT output
  requires listing them in ``--output-mqtt-topics`` even if they aren’t
  actually published (limitation).
- You can also use the generic mapping mode with ``--input-map-mqtt-topics``
  for structured payloads (see ``examples/distributed/mqtt_dist_echo.lola``).

Redis I/O
---------

Use Redis as a transport for input and/or output.

Example::

  cargo run -- examples/simple_add.lola --input-redis-topics x y --output-redis-topics z

Publish JSON messages to Redis channels ``x`` and ``y`` that match the
value format (e.g., using ``redis-cli``), and subscribe to ``z`` to read
outputs.

ROS 2 I/O (feature)
-------------------

ROS 2 support is behind the ``ros`` feature and uses a mapping file that
binds ROS topics and message fields to stream variables. Build and run::

  cargo run --features ros -- --input-ros-topics examples/counter_ros_map.json examples/counter.lola

In another ROS 2-sourced terminal, publish::

  ros2 topic pub /x std_msgs/msg/Int32 "{data: 1}"

The monitor should begin counting. You must have sourced ROS 2 Humble
and built the custom message interfaces if required (see Docker section).

Distributed execution
---------------------

The tool supports several distributed modes coordinated over MQTT.
You can use the provided EMQX service in ``docker/docker-compose.yaml``.

Centralised monitor (default)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No extra flags are needed; this is the default.

Localised monitor
^^^^^^^^^^^^^^^^^

Run a local monitor for variables assigned to a given node in a
distribution graph. Provide the graph and your local node id::

  cargo run -- examples/simple_add.lola \
    --distribution-graph examples/simple_add_distribution_graph.json \
    --local-node A \
    --output-stdout

Alternatively, specify variables directly for local monitoring::

  cargo run -- examples/simple_add.lola --local-topics x y --output-stdout

MQTT-based distributed modes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Centralised distributed over locations::

    cargo run -- examples/simple_add.lola --mqtt-centralised-distributed A B C --output-stdout

- Randomised distributed over locations::

    cargo run -- examples/simple_add.lola --mqtt-randomized-distributed A B C --output-stdout

- Static or dynamic optimisation (requires constraints variables)::

    cargo run -- examples/simple_add_distributable.lola \
      --mqtt-static-optimized A B C \
      --distribution-constraints w v \
      --output-stdout

    cargo run -- examples/simple_add_distributable.lola \
      --mqtt-dynamic-optimized A B C \
      --distribution-constraints w v \
      --output-stdout

Waiting for scheduler assignment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A node can wait to receive its assignment from a scheduler via MQTT::

  cargo run -- examples/simple_add_distributable.lola --distributed-work --local-node A --output-stdout

Work scheduler
^^^^^^^^^^^^^^

A separate binary, ``work_scheduler``, can compute and send assignments.
Run it with a distribution graph::

  cargo run --bin work_scheduler -- --distribution-graph examples/simple_add_distribution_graph.json

Docker support
--------------

A multi-stage Dockerfile is provided:

- ``docker/Dockerfile`` has two targets:

  - ``base``: ROS 2 Humble + tooling + custom interfaces build
  - ``dev``: adds a non-root user and installs Rust toolchain

- ``docker/DockerfileDeploy`` builds and runs the release binary.

A compose file starts EMQX and a dev container:

- Start EMQX only::

    docker compose -f docker/docker-compose.yaml up -d emqx

- Start dev environment (includes Rust)::

    docker compose -f docker/docker-compose.yaml up -d dev emqx

The dev container runs ``sleep infinity``; exec into it to build and run
with Cargo. ROS 2 Humble is available in the base image. The
``ros_interfaces`` are built during image creation.

Examples gallery
----------------

- ``examples/simple_add.lola`` — integer addition
- ``examples/simple_add_typed.lola`` — typed variant
- ``examples/past.lola``, ``examples/future.lola`` — temporal operators
- ``examples/dynamic_lola/*.lola`` — dynamic features like ``eval`` and
  ``default``
- ``examples/distributed/*.lola`` — distributed MQTT examples

Troubleshooting
---------------

- MQTT or Redis connection issues

  - Check broker/server is running and reachable
  - Set explicit ports via ``--mqtt-port`` / ``--redis-port`` if needed

- Parser/language

  - Default parser mode is ``combinator`` and language is ``dynsrv`` (LOLA
    alias). Use ``--parser-mode`` and ``--language`` if necessary.

- Logging

  - Increase verbosity with ``RUST_LOG=debug`` when diagnosing issues.

Further reading
---------------

- Source code for I/O backends: ``src/io``
- CLI definitions and flags: ``src/cli/args.rs``
- Runtime builder and distribution modes: ``src/runtime/builder.rs``
- Examples and fixtures: ``examples/``

Acknowledgement
---------------

The work presented here is supported by the RoboSAPIENS project funded by
the European Commission's Horizon Europe programme under grant agreement
number 101133807.
