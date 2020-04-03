from flask import Blueprint
from app import data, utility
import json

api = Blueprint('api', __name__)


# api load and clean route
@api.route('/today')
def today():
    return data.download_dict('today')


@api.route('/cases')
def cases():
    return data.download_list('cases')


@api.route('/timeline')
def timeline():
    return data.download_list('timeline')


@api.route('/risks')
def risks():
    return data.download_list('area')
