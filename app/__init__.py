# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask_cors import CORS
from app import route
from app.api import api

# Initialize application
app = Flask(__name__)
app.register_blueprint(api)

# configuration
app_settings = os.getenv(
    'APP_SETTINGS',
    'app.config.DevelopmentConfig'
)
app.config.from_object(app_settings)


# Dev Config
# app.config.from_object(__name__)
DEBUG = True

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})




