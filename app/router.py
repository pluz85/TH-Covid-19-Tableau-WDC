from app import export_data
from flask import jsonify, render_template, Blueprint

router = Blueprint('router', __name__)

headers = {
    'json': 'true',
    'Content-Type': 'application/json; charset=utf-8',
}


# sanity check route
@router.route('/')
def index():
    return render_template('index.html')


@router.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@router.route('/download-cases', methods=['GET'])
def cases_download():
    return export_data.download('cases')


@router.route('/download-risks', methods=['GET'])
def risks_download():
    return export_data.download('risks')


@router.route('/download-timeline', methods=['GET'])
def timeline_download():
    return export_data.download('timeline')


@router.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
