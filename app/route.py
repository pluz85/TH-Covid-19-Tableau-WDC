from app import app, export_data
from flask import jsonify, render_template

headers = {
    'json': 'true',
    'Content-Type': 'application/json; charset=utf-8',
}


# sanity check route
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/download-cases', methods=['GET'])
def cases_download():
    return export_data.download('cases')


@app.route('/download-risks', methods=['GET'])
def risks_download():
    return export_data.download('risks')


@app.route('/download-timeline', methods=['GET'])
def timeline_download():
    return export_data.download('timeline')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
