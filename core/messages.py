from dataclasses import dataclass
from typing import List

@dataclass
class Twist:
    v: float = 0.0   # linear velocity [m/s]
    w: float = 0.0   # angular velocity [rad/s]

@dataclass
class Pose2D:
    x: float = 0.0
    y: float = 0.0
    yaw: float = 0.0  # radians

@dataclass
class LaserScan:
    ranges: List[float]
    angles: List[float]
