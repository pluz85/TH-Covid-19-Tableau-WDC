from flask import Blueprint
from app import data_min as d

api = Blueprint('api', __name__)
endpoints = ['today', 'cases', 'timeline', 'risks']


@api.route('/<endpoint>')
def get_endpoint(endpoint):
    if endpoint in endpoints:
        if endpoint == 'today':
            return d.dict(endpoint)
        else:
            return d.list(endpoint)
    else:
        return d.res_err()

# # api load and clean route
# @api.route('/today')
# def today(): return d.dict('today')
#
#
# @api.route('/cases')
# def cases(): return d.list('cases')
#
#
# @api.route('/timeline')
# def timeline(): return d.list('timeline')
#
#
# @api.route('/area')
# def risks(): return d.list('area')


@api.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response
