from app import export_data_min as e, status as s
from flask import render_template as r, Blueprint

# import pandas as pd

router = Blueprint('router', __name__)


@router.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


@router.route('/')
def index():
    status = s.status_date()
    return r('index.html', spanCode=status)


@router.route('/download-cases', methods=['GET'])
def cases_download():
    return e.dl('cases')


@router.route('/download-risks', methods=['GET'])
def risks_download():
    return e.dl('risks')


@router.route('/download-timeline', methods=['GET'])
def timeline_download():
    return e.dl('timeline')


@router.errorhandler(404)
def page_not_found(e):
    return r('404.html'), 404
