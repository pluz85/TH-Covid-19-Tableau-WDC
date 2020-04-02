# -*- coding: utf-8 -*-

from flask import Flask
from flask_cors import CORS
from app import route
from app.api import api

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.register_blueprint(api)
# Dev Config
# app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})




