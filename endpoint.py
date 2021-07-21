import flask
from flask import request
import urllib.request
from PIL import Image
  
app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "Nothing seems to be here", 404

@app.route('/image', methods=['POST'])
def image():
    requestbody = request.get_json(force=True)
    return "404, not found", 404

@app.route('/image/slap', methods=['POST'])
def image_slap():
    requestbody = request.get_json(force=True)

    avatarURL = "avatarURL" in requestbody
    
    if avatarURL:
        if (type(requestbody["avatarURL"]) is list):
            if len(requestbody["avatarURL"]) == 2:
                if r"https://cdn.discordapp.com/avatars/" in requestbody["avatarURL"][0] and r"https://cdn.discordapp.com/avatars/" in requestbody["avatarURL"][1]:
                        return "200, OK", 200
    
    return "400, bad request", 400

@app.errorhandler(400)
def bad_request(e):
    return "400, bad request", 400

print("running app")
app.run()
