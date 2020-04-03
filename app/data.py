import requests
import json
from app import utility

headers = {
    'json': 'true',
    'Content-Type': 'application/json; charset=utf-8',
}
url = 'https://covid19.th-stat.com/api/open/'


def download_dict(endpoint):
    response = requests.get(url + endpoint, headers=headers)
    if response.status_code == 200:
        data = response.json()
        utility.clean_dict(data)
        return data


def download_list(endpoint):
    response = requests.get(url + endpoint, headers=headers)
    if response.status_code == 200:
        data = response.json()['Data']
        utility.clean_list(data)
        return json.dumps(data)

