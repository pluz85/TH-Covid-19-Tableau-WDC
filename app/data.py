import requests
import json
from app import utility

headers = {'json': 'true', 'Content-Type': 'application/json; charset=utf-8'}
url = 'https://covid19.th-stat.com/api/open/'


def download_dict(endpoint):
    response = requests.get(url + endpoint, headers=headers)
    if response.status_code == 200:
        data = response.json()
        utility.c_dict(data)
        return data


def download_list(endpoint):
    response = requests.get(url + endpoint, headers=headers)
    if response.status_code == 200:
        data = response.json()['Data']
        utility.c_list(data)
        return json.dumps(data)


def res_err():
    return json.dumps({"error": "Not found"})
