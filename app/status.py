import requests
import pandas as pd


headers = {
    'json': 'true',
    'Content-Type': 'application/json; charset=utf-8',
}
url = 'https://covid19.th-stat.com/api/open/'


def download_date():
    endpoints = ['today', 'timeline', 'cases', 'area']
    dateKeywords = ['UpdateDate', 'LastData']
    source = ['ข้อมูลประจำวัน', 'สรุปตามช่วงเวลา', 'ข้อมูลแต่ละเคส', 'แจ้งเตือนพื้นที่']
    dateTime = []
    for endpoint in endpoints:
        response = requests.get(url + endpoint, headers=headers)
        if response.status_code == 200:
            for dateKeyword in dateKeywords:
                try:
                    date = response.json()[dateKeyword]
                    dateTime.append(date)
                    # return date
                except KeyError:
                    pass
    dfPrep = dict(zip(source, dateTime))
    return dfPrep
