import math
from core.messages import Pose2D, Twist

class DiffDriveRobot:
    def __init__(self, name="robot", init_pose=Pose2D(), radius=0.2, cmd_topic="/cmd_vel"):
        self.name = name
        self.pose = Pose2D(init_pose.x, init_pose.y, init_pose.yaw)
        self.radius = radius
        self.cmd_topic = cmd_topic

        self.traj_x = [self.pose.x]
        self.traj_y = [self.pose.y]

    def update(self, dt, cmd: Twist):
        v = cmd.v
        w = cmd.w

        self.pose.x += v * math.cos(self.pose.yaw) * dt
        self.pose.y += v * math.sin(self.pose.yaw) * dt
        self.pose.yaw += w * dt

        # Normalize angle
        self.pose.yaw = (self.pose.yaw + math.pi) % (2*math.pi) - math.pi

        self.traj_x.append(self.pose.x)
        self.traj_y.append(self.pose.y)

def stop(self):
    self.pose = self.pose  # no change, just semantic
