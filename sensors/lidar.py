import math
from core.messages import LaserScan

class Lidar2D:
    def __init__(self, robot, obstacles, num_beams=36, max_range=4.0):
        self.robot = robot
        self.obstacles = obstacles
        self.num_beams = num_beams
        self.max_range = max_range
        self.angles = [i * (2*math.pi/num_beams) for i in range(num_beams)]
        self.topic = "/scan"

    def cast_ray(self, angle):
        # Ray marching
        step = 0.1
        r = 0.0
        x0, y0, yaw = self.robot.pose.x, self.robot.pose.y, self.robot.pose.yaw
        global_angle = yaw + angle

        while r < self.max_range:
            r += step
            x = x0 + r * math.cos(global_angle)
            y = y0 + r * math.sin(global_angle)

            # Check collision with obstacles
            for obs in self.obstacles:
                if obs.distance_to(x, y) < 0:
                    return r
        return self.max_range

    def scan(self):
        ranges = [self.cast_ray(a) for a in self.angles]
        return LaserScan(ranges=ranges, angles=self.angles)
