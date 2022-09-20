from argparse import ArgumentParser
from flask import Flask, request
from flask_pydantic import validate
from contracts import InputModel

app = Flask(__name__)


@app.route('/query_hello', methods=['GET'])
@validate()
def query_hello(query: InputModel):
    return f'Hello, {query.name}!'


@app.route('/param_hello/<name>', methods=['GET'])
@validate()
def param_hello(name: str):
    return f'Hello, {name}!'


@app.route('/body_hello', methods=['POST'])
@validate()
def body_hello(body: InputModel):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        return f'Hello, {body.name}!'
    else:
        return 'Content-Type not supported!'


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--host', type=str, default='localhost')
    parser.add_argument('--port', type=int, default=5000)
    args = parser.parse_args()

    app.run(host=args.host, port=args.port)
