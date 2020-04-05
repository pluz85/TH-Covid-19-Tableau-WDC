import re
import datetime
from pythainlp.util import thai_strftime

html_tag = r'.*<.*?>'
common = r'\"'
datetime_str = r'[0-3]\d/[01]\d/(19|20)\d{2}\s[0-2]\d:[0-5]\d'
date_str = r'[0-3]\d/[01]\d/(19|20)\d{2}'
th_datetime_fmt = '%d %B %Y เวลา %H:%M น.'
th_date_fmt = '%d %B %Y'


# Cleaning Function
def c_dict(d):
    for k, v in d.items():
        if re.search(html_tag, str(v), 0):
            d[k] = re.sub(html_tag, '', v)
        elif re.search(common, str(v), 0):
            d[k] = re.sub(common, '', v, 0)
        else:
            pass
    return d


def c_list(lst):
    for i in range(0, len(lst)):
        c = lst[i]
        c_dict(c)
    return lst


def dt_re(kw):
    if re.search(datetime_str, kw, 0):
        date = datetime.datetime.strptime(kw, '%d/%m/%Y %H:%M')
        return thai_strftime(date, th_datetime_fmt)
    elif re.search(date_str, kw, 0):
        date = datetime.datetime.strptime(kw, '%d/%m/%Y')
        return thai_strftime(date, th_date_fmt)
    else:
        pass
