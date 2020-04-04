# -*- coding: utf-8 -*-

from flask import Flask
from flask_cors import CORS


def create_app():
    # Initialize application
    app = Flask(__name__)
    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})
    # Dev Config
    app.config.from_object(__name__)
    with app.app_context():
        from . import api, router
        app.register_blueprint(api)
        app.register_blueprint(router)
    return app




