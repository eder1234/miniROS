import math

def wrap_angle(theta):
    return (theta + math.pi) % (2*math.pi) - math.pi
