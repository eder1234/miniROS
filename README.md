# 📘 **README.md — miniROS**

A lightweight, educational robotics framework designed to teach the fundamentals of **ROS-like concepts** in an environment that runs **entirely in Google Colab** — without installing ROS or Gazebo.

`miniROS` provides simplified versions of:

* Nodes
* Topics
* Messages
* `cmd_vel` differential-drive robots
* Lidar sensing
* Obstacles and world simulation
* Occupancy grid mapping
* Local navigation (go-to-goal + obstacle avoidance)
* A geometric **safety layer** to prevent collisions

It is intentionally minimal, readable, and easy to extend.

---

# 🌟 Features

### ✔ **Core ROS-like abstractions**

* `Node` class with `step(dt)`
* `TopicManager` with publish / subscribe
* `/cmd_vel`, `/scan`, `/goal` topics
* Basic message types: `Pose2D`, `Twist`, `LaserScan`

### ✔ **2D differential-drive robot**

* Unicycle kinematics
* Trajectory recording
* Configurable radius
* Smooth motion integration (`dt = 0.05` default)

### ✔ **2D Lidar**

* Configurable number of beams
* Ray–obstacle intersections
* No noise (for clarity)

### ✔ **Obstacles**

* Circular obstacles
* Easily extended to polygons

### ✔ **Visualization**

* Static trajectory plots
* GIF animation support (via `matplotlib.animation`)
* Occupancy grid visualization

### ✔ **Mapping**

* Simple occupancy grid mapping
* Raytracing for free/occupied cells

### ✔ **Navigation**

* Waypoint manager (`/goal`)
* Local planner
* Soft repulsive-field obstacle avoidance
* **Hard safety layer** to prevent the robot from entering obstacles

---

# 📂 Project Structure

```
miniROS/
    core/
        node.py          # Base Node class
        topic.py         # Topic manager
        simulator.py     # Main simulation loop
        messages.py      # Pose2D, Twist, LaserScan

    robots/
        diffdrive.py     # Differential-drive robot model

    sensors/
        lidar.py         # 2D Lidar

    world/
        obstacles.py     # Circular obstacles
        occupancy_grid.py# Mapping grid

    notebooks/
        01_teleop.ipynb
        02_cmdvel_node.ipynb
        03_lidar_obstacles.ipynb
        04_mapping.ipynb
        05_navigation_pipeline.ipynb   # With safety layer
```

---

# 🚀 Usage in Google Colab

You can load the library directly from GitHub:

```python
!rm -rf miniROS
!git clone https://github.com/eder1234/miniROS.git
sys.path.append('/content/miniROS')
```

Then import modules:

```python
from core.simulator import MiniRosSimulator
from robots.diffdrive import DiffDriveRobot
from sensors.lidar import Lidar2D
from world.obstacles import CircleObstacle
from core.node import Node
from core.messages import Pose2D, Twist
```

---

# 📘 Teaching Curriculum (5 Notebooks)

### **Notebook 1 — Teleoperation**

* Introduces topics and `cmd_vel`
* Students manually control the robot with linear/angular velocities
* Basic simulation and plotting

### **Notebook 2 — Autonomy via `ExampleNode`**

* Students write a node that publishes commands automatically
* Introduces node lifecycle and simulation loop

### **Notebook 3 — Lidar + Obstacles**

* Ray-based lidar simulation
* Visualization of circular obstacles
* Students experiment with obstacle placement and robot behavior

### **Notebook 4 — Occupancy Grid Mapping**

* Lidar → Occupancy grid mapping
* Raytracing for free/occupied cells
* Visual map building
* First introduction to perception

### **Notebook 5 — Navigation Pipeline**

* Goal publishing (`/goal`) via `GoalManagerNode`
* Local planner (`GoToGoalNode`) with proportional controller
* Smooth obstacle avoidance using repulsive fields
* **Hard collision safety layer**:
  If the next pose would enter an obstacle → stop + rotate until safe
* Final trajectory visualization

This notebook mimics ROS concepts:

* global planner
* local planner
* sensor feedback
* safety override

---

# 🛡 Safety Layer (Option A — Stop + Rotate)

The safety layer prevents collisions by predicting the robot’s **next** pose before it is applied:

```python
if next_pose_inside_obstacle:
    v = 0
    w = +1.0  # rotate left until safe
```

This guarantees:

* No collision
* Stable convergence
* Easy-to-understand behavior for students

---

# 🧪 Extending miniROS

Possible student projects:

* Add noise to lidar
* Add polygons or walls
* Implement PID instead of P-control
* Add a global planner (RRT, PRM, A*)
* Implement wall-following behavior
* Multi-robot topics
* Simulate communication delays

---

# 📄 License

MIT License — free to use, modify, distribute.

---

# 🤝 Contributing

Pull requests are welcome — especially from students after completing exercises.


Just tell me.
