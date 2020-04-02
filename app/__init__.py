# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask_cors import CORS
from app import router
from app.api import api
from app.router import router

# Initialize application
app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(router)

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




