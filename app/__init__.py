# -*- coding: utf-8 -*-

from flask import Flask
from flask_cors import CORS
from app import router
from app.api import api
from app.router import router


def create_app():
    # Initialize application
    app = Flask(__name__)
    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})
    # Dev Config
    app.config.from_object(__name__)
    with app.app_context():
        app.register_blueprint(api)
        app.register_blueprint(router)
    return app




