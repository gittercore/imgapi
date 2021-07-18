import flask
from flask import request

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "Nothing seems to be here", 404

@app.route('/', methods=['POST'])
def create():
    requestbody = request.get_json(force=True)
    return requestbody, 404

@app.errorhandler(400)
def bad_request(e):
    return "400, bad request", 400

print("running app")
app.run()
