# -*- coding: utf-8 -*-

from flask import Flask
from flask_htmlmin import HTMLMIN
from flask_cors import CORS

# Initialize application
app = Flask(__name__)
# Minify HTML
htmlmin = HTMLMIN(app)
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
# app.config.from_object(__name__)
app.config.from_object('app.config.Config')
app.config.from_object('app.config.DevConfig')
with app.app_context():
    from .router import api, router
    app.register_blueprint(api)
    app.register_blueprint(router)
