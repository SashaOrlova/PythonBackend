class Topic:
    text: int

    def __init__(self, text):
        self.text = text


class Comment:
    topic_id: int
    text: int

    def __init__(self, topic_id, text):
        self.text = text
        self.topic_id = topic_id
