import numpy as np
import math

class OccupancyGridMap:
    """
    Simple occupancy grid:
    - -1 = unknown
    -  0 = free
    -  1 = occupied
    """
    def __init__(self, width=200, height=200, resolution=0.05):
        self.width = width
        self.height = height
        self.resolution = resolution
        self.grid = -1 * np.ones((height, width), dtype=np.int8)

        # Origin in the center of the grid
        self.cx = width // 2
        self.cy = height // 2

    def world_to_grid(self, x, y):
        gx = int(self.cx + x / self.resolution)
        gy = int(self.cy - y / self.resolution)
        if 0 <= gx < self.width and 0 <= gy < self.height:
            return gx, gy
        return None, None

    def set_occupied(self, x, y):
        gx, gy = self.world_to_grid(x, y)
        if gx is not None:
            self.grid[gy, gx] = 1

    def set_free(self, x, y):
        gx, gy = self.world_to_grid(x, y)
        if gx is not None:
            self.grid[gy, gx] = 0

    def raytrace(self, x0, y0, x1, y1, steps=30):
        """
        Marks free cells along the ray from (x0,y0) to (x1,y1).
        """
        for i in range(steps):
            t = i / steps
            xi = x0 + t*(x1 - x0)
            yi = y0 + t*(y1 - y0)
            self.set_free(xi, yi)
