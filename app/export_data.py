from flask import current_app, send_file
import json
import pandas as pd
import io
import datetime


def get_json_response(endpoint, **kwargs):
    view = current_app.view_functions['api.get_endpoint']
    res = view(endpoint, **kwargs)
    js = json.loads(res)
    return js


def to_excel(data, endpoint):
    export = pd.DataFrame(data)
    strIO = io.BytesIO()
    excel_writer = pd.ExcelWriter(strIO, engine="xlsxwriter")
    export.to_excel(excel_writer, sheet_name=endpoint, index=False, header=True, encoding='utf-8')
    excel_writer.save()
    strIO.getvalue()
    strIO.seek(0)
    return strIO


def download(endpoint):
    d = (datetime.date.today() + datetime.timedelta(hours=11)).strftime('%d%m%Y')  # Heroku Server Location Time Diff
    filename = endpoint + '_' + d
    api = get_json_response(endpoint)
    data = to_excel(api, endpoint)
    return send_file(data,
                     attachment_filename=filename + '.xlsx',
                     as_attachment=True)
