from app import export_data_min as e
from flask import render_template as r, Blueprint

# import pandas as pd

router = Blueprint('router', __name__)


@router.route('/')
def index():
    # df = pd.DataFrame.from_dict(status.download_date(), orient='index')
    return r('index.html')


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
