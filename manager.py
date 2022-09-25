from db import DB
from objects import Topic, Comment


class Manager:
    def __init__(self):
        self.bd = DB()

    def add_topic(self, text: str):
        if len(text) == 0:
            raise Exception("empty topic text")

        return self.bd.create_topic(Topic(text))

    def add_comment(self, topic_id: int, text: str):
        if len(text) == 0:
            raise Exception("empty comment text")
        if topic_id > self.bd.get_topic_number():
            raise Exception("wrong topic id")

        return self.bd.create_comment(Comment(topic_id - 1, text))

    def get_comments(self, topic_id):
        if topic_id > self.bd.get_topic_number():
            raise Exception("wrong topic id")

        return self.bd.get_comments(topic_id - 1)
