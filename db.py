from objects import Comment, Topic


class DB:
    def __init__(self):
        # connections in future
        self.comments = []
        self.topics = []

    def create_comment(self, comment: Comment):
        self.comments.append(comment)
        return len(self.comments)

    def create_topic(self, topic: Topic):
        self.topics.append(topic)
        return len(self.topics)

    def get_comments(self, topic_id: int):
        return {
            'topic': self.topics[topic_id].text,
            'comments': [x.text for x in self.comments if x.topic_id == topic_id]
        }

    def get_topic_number(self):
        return len(self.topics)
