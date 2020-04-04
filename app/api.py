from flask import Blueprint
from app import data_min as d

api = Blueprint('api', __name__)


@api.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


# api load and clean route
@api.route('/today')
def today(): return d.dict('today')


@api.route('/cases')
def cases(): return d.list('cases')


@api.route('/timeline')
def timeline(): return d.list('timeline')


@api.route('/risks')
def risks(): return d.list('area')
