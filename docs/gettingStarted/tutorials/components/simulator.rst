TurtleBot LiDAR Occlusion Simulator Tutorial
###########################################

**Repository:** `link <https://github.com/saharnn96/Turtlebot_LidarOcclusion_Simulator>`_


This tutorial explains the TurtleBot LiDAR Occlusion Simulator, a web-based dashboard application that simulates a TurtleBot4 robot with LiDAR sensor capabilities. You can test navigation algorithms, study LiDAR occlusion effects, and visualize robot movement in real-time.

Overview
========

The TurtleBot LiDAR Occlusion Simulator provides:

- **Real-time robot simulation** with position tracking
- **LiDAR sensor simulation** with configurable occlusion
- **Interactive web dashboard** built with Dash and Plotly
- **Multiple navigation modes** (Standard and Spin Configuration)
- **Path planning** using A* algorithm
- **MQTT/Redis communication** for external control
- **Live data visualization** with polar LiDAR plots and 2D maps

Prerequisites
-------------

- Python 3.7 or higher
- Redis server (optional, for external communication)
- Web browser (Chrome, Firefox, Safari, Edge)
- Required packages: ``pip install dash dash-bootstrap-components plotly numpy paho-mqtt redis rpio``

Getting Started
===============

1. **Clone or download** the repository containing ``dash_turtlebotsim.py``

2. **Install dependencies**:

   .. code-block:: bash

      pip install -r requirements.txt

3. **Run the simulator**:

   .. code-block:: bash

      python dash_turtlebotsim.py

4. **Open your web browser** and navigate to ``http://localhost:8050``

Configuration
=============

**Environment Variables** (optional):

.. code-block:: bash

   # Set Redis connection (default: localhost:6379)
   set REDIS_HOST=localhost
   set REDIS_PORT=6379

   # Set Dash server configuration (default: 0.0.0.0:8050)
   set DASH_HOST=0.0.0.0
   set DASH_PORT=8050
   set DASH_DEBUG=False

**Optional: Set up Redis server** (for external communication):

.. code-block:: bash

   # On Windows (using Chocolatey)
   choco install redis-64

   # On Linux
   sudo apt-get install redis-server

   # On macOS
   brew install redis

Examples
========

1. **Start the simulator**:

   .. code-block:: bash

      python dash_turtlebotsim.py

2. **Open your web browser** and navigate to:

   .. code-block::

      http://localhost:8050

3. **The dashboard should load** showing:
   - Control panel (left)
   - Map visualization (center)
   - LiDAR data plot (right)

User Interface
==============

**Control Panel** (left side):

- **Status Indicators**: LiDAR status and navigation mode
- **Control Buttons**: Toggle LiDAR occlusion, navigation mode, stop navigation
- **Manual Navigation**: Target X/Y inputs and navigate button
- **Robot Status**: Current position, heading, navigation state, obstacles

**Map Visualization** (center):

- Robot position (blue circle with "TurtleBot4" label)
- Heading direction (blue arrow)  
- Planned trajectory (green dashed line)
- Obstacles (red X markers)
- **Interactive clicking** for navigation targets

LiDAR Data Plot
---------------

The right panel displays:

- **Polar plot** of LiDAR sensor readings
- **360-degree coverage** with distance measurements
- **Real-time updates** showing occlusion effects

Using the Simulator
===================

Basic Navigation
----------------

**Method 1: Click Navigation**

1. Click anywhere on the map visualization
2. The robot will automatically plan a path to that location
3. Watch the robot move along the generated trajectory

**Method 2: Manual Coordinates**

1. Enter X and Y coordinates in the input fields
2. Click "Navigate to Target"
3. The robot will navigate to the specified position

Testing LiDAR Occlusion
-----------------------

1. **Start with normal LiDAR**: Observe the red line in the polar plot
2. **Click "Toggle LiDAR Occlusion"**: Notice how readings change
3. **Observe the effects**: First 300 degrees show infinite readings
4. **Test navigation**: See how occlusion affects movement

Navigation Modes
----------------

**Standard Mode**
   - Normal point-to-point navigation
   - Direct movement along planned path
   - Publishes pose and scan data at each waypoint

**Spin Configuration Mode**
   - Enhanced navigation with rotation
   - Robot performs spinning motions during navigation
   - Useful for testing rotational sensors and algorithms

Advanced Features
=================

External Communication
----------------------

The simulator supports external control via Redis/MQTT:

**Topic Structure**:
   - ``/pose``: Robot position and orientation
   - ``/Scan``: LiDAR sensor data
   - ``/spin_config``: Navigation configuration commands

**Sending Commands**:

.. code-block:: python

   import json
   import redis

   # Connect to Redis
   r = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

   # Send spin configuration
   command = {
       "commands": [{
           "duration": 2.0,
           "omega": 45  # degrees
       }]
   }
   r.publish("/spin_config", json.dumps(command))

Logging and Monitoring
---------------------

The simulator provides comprehensive logging:

- **Console output**: Real-time status messages
- **Redis logging**: Centralized log storage
- **Event tracking**: Navigation events, mode changes, etc.

Customization
=============

Modifying Map Parameters
-----------------------

Edit the ``TurtleBotSim`` class initialization:

.. code-block:: python

   def __init__(self):
       self.map_size = 20  # Increase map size
       self.obstacles = self.generate_obstacles(num_obstacles=10)  # More obstacles

Adjusting Update Frequency
-------------------------

Modify the Dash interval component:

.. code-block:: python

   dcc.Interval(
       id='interval-component',
       interval=500,  # Update every 0.5 seconds
       n_intervals=0
   )

Customizing LiDAR Parameters
---------------------------

Edit the ``publish_scan`` method:

.. code-block:: python

   lidar_data = {
       'angle_min': -3.14159,  # Adjust scan range
       'angle_max': 3.14159,
       'angle_increment': 0.01745,  # Higher resolution
       'range_max': 15.0,  # Longer range
       'ranges': self.lidar_data
   }

Troubleshooting
===============

Common Issues
-------------

**Dashboard won't load**
   - Check if port 8050 is available
   - Verify all dependencies are installed
   - Look for error messages in console

**Redis connection errors**
   - Ensure Redis server is running
   - Check REDIS_HOST and REDIS_PORT environment variables
   - Simulator will work without Redis for basic functionality

**Navigation not working**
   - Check for JavaScript errors in browser console
   - Verify map coordinates are within bounds
   - Ensure navigation isn't already active

**Performance issues**
   - Reduce update frequency in interval component
   - Close other browser tabs
   - Check system resources

Development and Extension
========================

Code Structure
--------------

**Main Components**:
   - ``TurtleBotSim``: Core simulation logic
   - ``Dash app``: Web interface and callbacks
   - ``MQTT/Redis``: External communication
   - ``A* pathfinding``: Navigation algorithm

**Adding New Features**:

1. **New sensors**: Extend ``TurtleBotSim`` class
2. **UI components**: Add Dash components and callbacks
3. **Communication protocols**: Modify ``CommunicationManager`` usage
4. **Visualization**: Create new Plotly figures

Example Extensions
-----------------

**Adding Camera Simulation**:

.. code-block:: python

   def simulate_camera(self):
       # Generate synthetic camera data
       return {
           'image_data': np.random.rand(480, 640, 3),
           'timestamp': time.time()
       }

**Custom Path Planning**:

.. code-block:: python

   def rrt_pathfinding(start, goal, obstacles):
       # Implement RRT algorithm
       # Return optimized path
       pass

Troubleshooting
===============

**Common Issues:**

- **Port 8050 already in use**: Change the port in the Dash configuration or stop other applications using this port
- **Redis connection failed**: Ensure Redis server is running if using external communication features  
- **Dashboard not loading**: Check that all dependencies are installed correctly
- **LiDAR visualization issues**: Verify browser compatibility (Chrome/Firefox recommended)

**Additional Resources:**

The TurtleBot LiDAR Occlusion Simulator provides a comprehensive platform for testing robot navigation algorithms, studying sensor occlusion effects, and developing real-time monitoring dashboards.

For additional support or feature requests, refer to the project documentation.