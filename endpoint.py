import flask
from flask import request, json
import urllib.request
from PIL import Image
from workers.facepalm.facepalm import facepalm
from workers.punch.punch import punch
import os
import logging

logging.getLogger('werkzeug').disabled = True

app = flask.Flask(__name__)

os.environ['WERKZEUG_RUN_MAIN'] = 'true'

id = 0


@app.route('/', methods=['GET'])
def home():
    return "Nothing seems to be here", 404

@app.route('/image', methods=['POST'])
def image():
    requestbody = request.get_json(force=True)
    return "404, not found", 404

@app.route('/image/facepalm', methods=['POST'])
def image_slap():
    requestbody = request.get_json(force=True)

    avatarURL = "avatarURL" in requestbody
    
    if avatarURL:
        if (type(requestbody["avatarURL"]) is list):
            if len(requestbody["avatarURL"]) == 2:
                if r"https://cdn.discordapp.com/avatars/" in requestbody["avatarURL"][0] and r"https://cdn.discordapp.com/avatars/" in requestbody["avatarURL"][1]:
                        global id 
                        id += 1
                        facepalm_result_data = facepalm(requestbody["avatarURL"][0], requestbody["avatarURL"][1], id)
                        response = app.response_class(
                            response = json.dumps(facepalm_result_data),
                            status = 200, 
                            mimetype = "application/json"
                        )
                        return response, 200
    
    return "400, bad request", 400

@app.route('/image/punch', methods=['POST'])
def image_punch():
    requestbody = request.get_json(force=True)

    avatarURL = "avatarURL" in requestbody
    
    if avatarURL:
        if (type(requestbody["avatarURL"]) is list):
            if len(requestbody["avatarURL"]) == 2:
                if r"https://cdn.discordapp.com/avatars/" in requestbody["avatarURL"][0] and r"https://cdn.discordapp.com/avatars/" in requestbody["avatarURL"][1]:
                        global id 
                        id += 1
                        punch_result_data = punch(requestbody["avatarURL"][0], requestbody["avatarURL"][1], id)
                        response = app.response_class(
                            response = json.dumps(punch_result_data),
                            status = 200, 
                            mimetype = "application/json"
                        )
                        return response, 200
    
    return "400, bad request", 400

@app.errorhandler(400)
def bad_request(e):
    return "400, bad request", 400

print("running app")
app.run()
