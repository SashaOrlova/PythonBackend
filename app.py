from argparse import ArgumentParser
from flask import Flask
from flask_pydantic import validate
from contracts import CreateTopicModel, CreateCommentModel
from manager import Manager

app = Flask(__name__)
manager = Manager()


@app.route('/create_topic', methods=['POST'])
@validate()
def create_topic(body: CreateTopicModel):
    return {
        "topic_id": manager.add_topic(body.text)
    }


@app.route('/create_comment', methods=['POST'])
@validate()
def create_comment(body: CreateCommentModel):
    return {
        "comment_id": manager.add_comment(body.topic_id, body.text)
    }


@app.route('/get_topic/<topic_id>', methods=['GET'])
@validate()
def get_topic(topic_id: int):
    return manager.get_comments(topic_id)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--host', type=str, default='localhost')
    parser.add_argument('--port', type=int, default=5000)
    args = parser.parse_args()

    app.run(host=args.host, port=args.port)
