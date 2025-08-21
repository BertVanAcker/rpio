
Docker Orchestrator Tutorial
=======================================

**Repository:** `link <https://github.com/saharnn96/docker-orchestrator>`_

This tutorial will guide you through setting up and using the Docker Orchestrator system, which manages multiple containerized applications that communicate through Redis.

Overview
-----------

The Docker Orchestrator is a system that:

* Manages multiple containerized Python applications (app1, app2, app3)
* Uses Redis as a message broker and data store
* Provides centralized orchestration capabilities
* Supports dynamic building and deployment of applications

Project Structure
---------------------
::

    docker-orchestrator/
    ├── app1/
    │   ├── Dockerfile
    │   └── redis_script.py
    ├── app2/
    │   ├── Dockerfile
    │   └── redis_script.py
    ├── app3/
    │   ├── Dockerfile
    │   └── redis_script.py
    ├── orchestrator/
    │   ├── Dockerfile
    │   └── orchestrator.py
    ├── docker-compose.yml
    └── tutorial.rst

Prerequisites
-------------------

Before starting, ensure you have:

* Docker Desktop installed and running
* Docker Compose installed
* Git (optional, for version control)
* Basic understanding of Docker and containerization

Getting Started
-------------------

1. Clone or Download the Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If using Git:

.. code-block:: bash

    git clone <repository-url>
    cd docker-orchestrator

Or download and extract the files to a directory called ``docker-orchestrator``.

2. Understanding the Applications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each application (app1, app2, app3) is a Python script that:

* Connects to Redis using the ``REDIS_HOST`` environment variable
* Sends periodic messages to Redis with execution times and logs
* Runs in an infinite loop with different sleep intervals

**App1 Example:**

.. code-block:: python

    #!/usr/bin/env python3
    import redis
    import random
    import time
    import os

    # Connect to Redis
    r = redis.Redis(host=os.getenv("REDIS_HOST", "localhost"), port=6379, decode_responses=True)

    node = "app1"

    while True:
        now = time.time()
        
        # Set execution time
        r.set(f"{node}:execution_time", round(random.uniform(0.3, 1.5), 3))
        r.set(f"{node}:start_execution", now)
        # Add a log entry for demo
        r.rpush(f"{node}:logs", f"Test log entry from {node} at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        print(f"Sent Redis messages from {node} at {now}")
        time.sleep(3)  # Different sleep times for each app

3. Understanding the Orchestrator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The orchestrator service:

* Listens for commands via Redis
* Can build and deploy applications dynamically
* Manages the Docker environment
* Provides centralized control over all applications

Running the System
-------------------------

Method 1: Using Docker Compose (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Start all services:**

.. code-block:: bash

    docker-compose up

This will start:

* Redis server (accessible on port 6379)
* Orchestrator service
* App1, App2, and App3 containers

2. **Start services in detached mode:**

.. code-block:: bash

    docker-compose up -d

3. **View logs:**

.. code-block:: bash

    # View all logs
    docker-compose logs

    # View logs for specific service
    docker-compose logs app1

4. **Stop all services:**

.. code-block:: bash

    docker-compose down

Method 2: Running Individual Applications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also run individual applications for testing:

1. **Start Redis first:**

.. code-block:: bash

    docker run -d --name redis-server -p 6379:6379 redis:alpine

2. **Build and run a specific app:**

.. code-block:: bash

    cd app1
    docker build -t app1-standalone .
    docker run --link redis-server:redis -e REDIS_HOST=redis app1-standalone

3. **Connect to host Redis:**

.. code-block:: bash

    # If Redis is running on your host machine
    docker run -e REDIS_HOST=host.docker.internal app1-standalone

Network Configuration
---------------------------

The system supports different networking modes:

Bridge Network (Default)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Applications connect to Redis using ``host.docker.internal``:

.. code-block:: yaml

    environment:
      - REDIS_HOST=host.docker.internal

Host Network
~~~~~~~~~~~~~~~~~~~~

For direct host network access, add to docker-compose.yml:

.. code-block:: yaml

    services:
      app1:
        network_mode: host
        environment:
          - REDIS_HOST=localhost

Monitoring and Debugging
------------------------------

1. **Check Redis data:**

.. code-block:: bash

    # Connect to Redis CLI
    docker exec -it <redis-container-name> redis-cli

    # View keys
    KEYS *

    # Check specific app data
    GET app1:execution_time
    LRANGE app1:logs 0 -1

2. **Monitor container status:**

.. code-block:: bash

    docker-compose ps
    docker stats

3. **View application logs:**

.. code-block:: bash

    docker-compose logs -f app1

Customization
--------------------

Adding New Applications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Create a new app directory:**

.. code-block:: bash

    mkdir app4

2. **Create Dockerfile:**

.. code-block:: dockerfile

    FROM python:3.10-slim
    WORKDIR /app
    RUN pip install redis
    COPY redis_script.py /app/redis_script.py
    RUN chmod +x /app/redis_script.py
    CMD ["python3", "/app/redis_script.py"]

3. **Create redis_script.py with your logic**

4. **Add to docker-compose.yml:**

.. code-block:: yaml

    app4:
      build:
        context: ./app4
      container_name: app4
      depends_on:
        - redis
      environment:
        - REDIS_HOST=host.docker.internal

Modifying Application Behavior
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Edit the ``redis_script.py`` files to:

* Change sleep intervals
* Modify Redis data structure
* Add new functionality
* Change logging format

Environment Variables
-------------------------------

The system uses several environment variables:

* ``REDIS_HOST``: Redis server hostname (default: localhost)
* ``PYTHONUNBUFFERED``: Ensure Python output is not buffered
* ``COMPOSE_NAME``: Docker Compose project name
* ``NODES``: Comma-separated list of application nodes

Troubleshooting
----------------------

Common Issues
~~~~~~~~~~~~~~~~~~~~~~~~~~

**1. Redis Connection Errors:**

.. code-block::

    redis.exceptions.ConnectionError: Error connecting to Redis

**Solutions:**

* Ensure Redis is running: ``docker-compose ps``
* Check network configuration
* Verify ``REDIS_HOST`` environment variable

**2. Build Failures:**

.. code-block::

    ERROR: failed to solve: failed to read dockerfile

**Solutions:**

* Ensure Dockerfile exists in the correct directory
* Check file permissions
* Verify Docker syntax

**3. Port Conflicts:**

.. code-block::

    Error starting userland proxy: listen tcp 0.0.0.0:6379: bind: address already in use

**Solutions:**

* Stop existing Redis instances
* Change port in docker-compose.yml
* Use ``docker ps`` to check running containers

**4. Container Exits Immediately:**

**Solutions:**

* Check application logs: ``docker-compose logs <service-name>``
* Verify Python script syntax
* Ensure all dependencies are installed

Debugging Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    # Check running containers
    docker ps

    # View container logs
    docker logs <container-name>

    # Execute commands inside container
    docker exec -it <container-name> /bin/bash

    # Check Docker images
    docker images

    # Remove all containers and images (cleanup)
    docker system prune -a


Next Steps
-----------------------

After completing this tutorial, you can:

* Modify the applications to suit your specific needs
* Add monitoring and alerting capabilities
* Implement more sophisticated orchestration logic
* Deploy to production environments
* Integrate with CI/CD pipelines

For more advanced Docker and Redis features, consult the official documentation:

* `Docker Documentation <https://docs.docker.com/>`_
* `Redis Documentation <https://redis.io/documentation>`_
* `Docker Compose Documentation <https://docs.docker.com/compose/>`_