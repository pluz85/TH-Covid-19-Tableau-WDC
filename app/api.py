from flask import Blueprint
from app import data, utility
import json

api = Blueprint('api', __name__)


# api load and clean route
@api.route('/today')
def today():
    return data.download_dict('today')


@api.route('/cases', methods=['GET'])
def cases():
    return data.download_list('cases')


@api.route('/timeline', methods=['GET'])
def timeline():
    return data.download_list('timeline')


@api.route('/risks', methods=['GET'])
def risks():
    raw = data.download_not_clean('area')
    clean = json.dumps(utility.clean_list(raw))
    return clean
