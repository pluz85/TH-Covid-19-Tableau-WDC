import requests
import json

headers = {
    'json': 'true',
    'Content-Type': 'application/json; charset=utf-8',
}
url = 'https://covid19.th-stat.com/api/open/'


def download_dict(endpoint):
    response = requests.get(url + endpoint, headers=headers)
    if response.status_code == 200:
        data = response.content
        return data


def download_list(endpoint):
    response = requests.get(url + endpoint, headers=headers)
    if response.status_code == 200:
        data_raw = json.loads(response.content)
        data = data_raw['Data']
        return json.dumps(data)


def download_not_clean(endpoint):
    response = requests.get(url + endpoint, headers=headers)
    if response.status_code == 200:
        data_raw = json.loads(response.content)
        data = data_raw['Data']
        return data
