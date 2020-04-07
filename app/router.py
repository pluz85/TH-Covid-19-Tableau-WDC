from app import export_data as e, status as s, data as d
from flask import render_template as r, Blueprint
from flask.views import MethodView

router = Blueprint('router', __name__)
api = Blueprint('api', __name__)
endpoints = ['today', 'cases', 'timeline', 'area']


@router.route('/')
def index():
    status = s.status_date()
    return r('index.html', spanCode=status)


# Pluggable Views
# class CovidApi(MethodView):
#
#     def dispatch_request(self, endpoint):
#         if endpoint in endpoints:
#             if endpoint == 'today':
#                 return d.d_data(endpoint)
#             else:
#                 return d.d_data(endpoint)
#         else:
#             return d.res_err()

@api.route('/<endpoint>')
def get_endpoint(endpoint):
    if endpoint in endpoints:
        if endpoint == 'today':
            return d.d_data(endpoint)
        else:
            return d.d_data(endpoint)
    else:
        return d.res_err()


@router.route('/download-<endpoint>')
def download(endpoint):
    return e.download(endpoint)


@router.errorhandler(404)
def page_not_found(error):
    return r('404.html'), 404


@router.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response
