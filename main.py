import flask
from flask import request, json
import urllib.request
from PIL import Image
from workers.facepalm.facepalm import facepalm
from workers.punch.punch import punch
import os
import logging
from app import start_flask_app

start_flask_app() 

