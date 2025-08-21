Distributed Deployment
###############################

**Repository:** `link <https://github.com/saharnn96/Helloworld_York_Demo.git>`_

This tutorial demonstrates how to deploy RPIO components in a distributed architecture using the MAPLE-K (Monitor-Analysis-Plan-Execute-Knowledge) pattern. The example shows autonomous TurtleBot simulation with distributed microservices communicating through Redis messaging.

.. contents:: Table of Contents
   :depth: 2
   :local:

Overview
========

This distributed deployment showcases RPIO's capability to orchestrate multiple containerized services across different nodes. The system uses:

- **MAPLE-K Architecture**: Monitor, Analysis, Plan, Execute components with Knowledge base
- **Redis Messaging**: Asynchronous communication between distributed services
- **Container Orchestration**: Docker Compose for service management and scaling
- **Real-time Monitoring**: Integrated dashboard for system observability
- **TurtleBot Simulation**: Physics-based robotics environment

**Key Components:**
- Sensor monitoring service
- ML-based analysis engine  
- Path planning service
- Motion execution service
- Trust monitoring system
- Operations dashboard
- Simulation environment

Getting Started
===============

Prerequisites
-------------

- Docker Engine 20.10+
- Docker Compose v3.8+
- Minimum 4GB RAM
- Git

Setup and Deployment
--------------------

**1. Clone the Repository**::

   git clone https://github.com/saharnn96/Helloworld_York_Demo.git
   cd Helloworld_York_Demo/Realization

**2. Start the Distributed System**::

   # Deploy all services 
   docker-compose up --build 

**3. Access the System**:

- **Operations Dashboard**: http://localhost:8050
- **Simulation Environment**: http://localhost:8051
- **Redis Messaging**: redis://localhost:6379 (internal)

System Components
=================

The distributed system consists of several RPIO components communicating through Redis:

- **Monitor Service**: Collects sensor data from the TurtleBot simulation
- **Analysis Service**: Processes sensor data using ML algorithms for anomaly detection
- **Plan Service**: Generates navigation paths based on sensor analysis
- **Execute Service**: Controls robot movement and executes planned actions
- **Trust Service**: Monitors system behavior and validates component trustworthiness
- **Dashboard**: Provides real-time monitoring and system control interface
- **Simulation**: Physics-based TurtleBot environment for testing distributed algorithms

Configuration
=============

The system uses environment variables and YAML configuration files for distributed deployment:

.. code-block:: bash

   # Redis Configuration
   REDIS_HOST=localhost
   REDIS_PORT=6379
   REDIS_DB=0
   
   # Service Configuration
   DASHBOARD_PORT=8050
   SIMULATION_PORT=8051
   LOG_LEVEL=INFO


Multi-Node Deployment
=====================

To deploy across multiple machines:

1. **Setup Redis** on a central server accessible to all nodes
2. **Update configuration** to point to the central Redis instance
3. **Deploy components** on different machines using the same Docker Compose files
4. **Configure networking** to allow communication between nodes

Monitoring and Troubleshooting
==============================

**Check System Health**::

   # View all service status
   docker-compose ps
   
   # Test Redis connectivity
   docker-compose exec redis redis-cli ping
   
   # Monitor specific service
   docker-compose logs --tail=50 monitor

**Common Issues**:

- **Port conflicts**: Ensure ports 8050, 8051, and 6379 are available
- **Memory issues**: Increase Docker memory allocation if services fail
- **Network connectivity**: Verify Redis connection between services

Use Case Benefits
=================

This distributed deployment use case demonstrates several key RPIO capabilities:

**Scalability**: Components can be scaled independently based on workload demands

**Fault Tolerance**: Individual service failures don't affect the entire system  

**Modularity**: Each MAPLE-K component is independently deployable and maintainable

**Real-time Monitoring**: Integrated trust monitoring ensures system reliability

**Production Ready**: Container-based deployment suitable for production environments

**Multi-node Support**: Architecture easily extends to true distributed deployment across multiple machines

This example showcases how RPIO enables building robust, scalable robotics systems using modern distributed architecture patterns.