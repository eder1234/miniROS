# miniROS

miniROS is a lightweight, educational ROS-like framework designed
to run inside Google Colab or Jupyter notebooks.

It teaches:
- nodes
- topics
- pub/sub messaging
- differential-drive robots
- `cmd_vel`
- simple 2D simulation
- trajectory visualization

Perfect for robotics teaching without needing ROS installation.

## Usage

In Google Colab:

```python
!git clone https://github.com/yourname/miniROS.git
import sys
sys.path.append('/content/miniROS')

from core.simulator import MiniRosSimulator
from robots.diffdrive import DiffDriveRobot
from nodes.circle_motion import CircleMotionNode

sim = MiniRosSimulator(dt=0.05)
robot = DiffDriveRobot()
controller = CircleMotionNode(v=0.2, w=0.4)

sim.add_robot(robot)
sim.add_node(controller)
sim.animate()
```
## Structure

core/: simulator, message types, node class, topic manager

robots/: robot definitions (currently differential-drive)

nodes/: example ROS-like controller nodes

utils/: geometry helpers and visualization utilities