from flask import Blueprint
from app import data as d

api = Blueprint('api', __name__)
endpoints = ['today', 'cases', 'timeline', 'area']


@wdc_api.route('/<endpoint>')
def get_endpoint(endpoint):
    if endpoint in endpoints:
        if endpoint == 'today':
            return d.d_dict(endpoint)
        else:
            return d.d_list(endpoint)
    else:
        return d.res_err()


@wdc_api.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response
