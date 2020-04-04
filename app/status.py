import requests

headers = {'json': 'true', 'Content-Type': 'application/json; charset=utf-8'}
url = 'https://covid19.th-stat.com/api/open/'


def status_date():
    endpoints = ['today', 'timeline', 'cases', 'area']
    source = ['ข้อมูลประจำวัน', 'สรุปตามช่วงเวลา', 'ข้อมูลแต่ละเคส', 'แจ้งเตือนพื้นที่']
    statusList = []
    for i in range(0, len(endpoints)):
        response = requests.get(url + endpoints[i], headers=headers)
        code = response.status_code
        if code == 200:
            s_code = str(code) + ' ✔'
            try:
                date = response.json()['UpdateDate']
                span = 'api ' + source[i] + '  Status Code: ' + s_code + '   Update At: ' + date
                statusList.append(span)
            except KeyError:
                span = 'api ' + source[i] + '  Status Code: ' + s_code + '   Update At: 💥 Missing Information'
                statusList.append(span)
        else:
            s_code = str(code) + ' ❌'
            span = 'api ' + source[i] + '  Status Code: ' + s_code
            statusList.append(span)
    return statusList
