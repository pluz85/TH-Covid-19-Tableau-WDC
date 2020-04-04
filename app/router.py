from app import export_data as e, status as s, data as d
from flask import render_template as r, Blueprint

router = Blueprint('router', __name__)
api = Blueprint('api', __name__)
endpoints = ['today', 'cases', 'timeline', 'area']


@router.route('/')
def index():
    status = s.status_date()
    return r('index.html', spanCode=status)


@api.route('/<endpoint>')
def get_endpoint(endpoint):
    if endpoint in endpoints:
        if endpoint == 'today':
            return d.d_dict(endpoint)
        else:
            return d.d_list(endpoint)
    else:
        return d.res_err()


@router.route('/download-<endpoint>')
def download(endpoint):
    return e.download(endpoint)


@router.errorhandler(404)
def page_not_found(e):
    return r('404.html'), 404


@router.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response
