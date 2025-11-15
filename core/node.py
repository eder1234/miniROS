class Node:
    """
    Base class for miniROS nodes.
    Override step(self, dt) to compute actions.
    """
    def __init__(self, name="unnamed"):
        self.name = name
        self._sim = None

    def _attach_sim(self, sim):
        self._sim = sim

    def publish(self, topic: str, msg):
        if self._sim is None:
            raise RuntimeError("Node is not attached to a simulator.")
        self._sim.topics.publish(topic, msg)

    def read_topic(self, topic: str, default=None):
        if self._sim is None:
            raise RuntimeError("Node is not attached to a simulator.")
        msg = self._sim.topics.read(topic)
        return msg if msg is not None else default

    def step(self, dt: float):
        pass

