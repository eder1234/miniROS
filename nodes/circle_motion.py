from core.node import Node
from core.messages import Twist

class CircleMotionNode(Node):
    def __init__(self, name="circle_motion", topic="/cmd_vel", v=0.3, w=0.3):
        super().__init__(name)
        self.topic = topic
        self.v = v
        self.w = w

    def step(self, dt):
        self.publish(self.topic, Twist(self.v, self.w))
