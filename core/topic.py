class Topic:
    def __init__(self, name: str):
        self.name = name
        self.message = None

class TopicManager:
    def __init__(self):
        self._topics = {}

    def get_topic(self, name: str):
        if name not in self._topics:
            self._topics[name] = Topic(name)
        return self._topics[name]

    def publish(self, name: str, msg):
        topic = self.get_topic(name)
        topic.message = msg

    def read(self, name: str):
        topic = self.get_topic(name)
        return topic.message
