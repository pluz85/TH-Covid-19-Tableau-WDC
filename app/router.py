from app import export_data_min as e, status as s
from flask import render_template as r, Blueprint

# import pandas as pd

router = Blueprint('router', __name__)


@router.route('/')
def index():
    status = s.status_date()
    return r('index.html', spanCode=status)


@router.route('/download-cases')
def cases_download():
    return e.dl('cases')


@router.route('/download-area')
def risks_download():
    return e.dl('area')


@router.route('/download-timeline')
def timeline_download():
    return e.dl('timeline')


@router.errorhandler(404)
def page_not_found(e):
    return r('404.html'), 404


@router.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response
