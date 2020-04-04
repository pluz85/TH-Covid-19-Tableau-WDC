import requests

headers = {'json': 'true', 'Content-Type': 'application/json; charset=utf-8'}
url = 'https://covid19.th-stat.com/api/open/'


def status_date():
    endpoints = ['today', 'timeline', 'cases', 'area']
    source = ['ข้อมูลประจำวัน', 'สรุปตามช่วงเวลา', 'ข้อมูลแต่ละเคส', 'แจ้งเตือนพื้นที่']
    statusList = []
    for i in range(0, len(endpoints)):
        response = requests.get(url + endpoints[i], headers=headers)
        if response.status_code == 200:
            code = str(response.status_code)
            try:
                date = response.json()['UpdateDate']
                span = 'api ' + source[i] + '  Status Code: ' + code + '   Update At: ' + date
                print(span)
                statusList.append(span)
            except KeyError:
                pass
    return statusList
