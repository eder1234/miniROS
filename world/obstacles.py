import math

class CircleObstacle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def distance_to(self, px, py):
        return math.sqrt((px - self.x)**2 + (py - self.y)**2) - self.radius
