import re

html_tag = r'.*<.*?>'
common = r'\"'


# Cleaning Function
def clean_dict(d):
    for k, v in d.items():
        if re.search(html_tag, str(v), 0):
            d[k] = re.sub(html_tag, '', v)
        elif re.search(common, str(v), 0):
            d[k] = re.sub(common, '', v, 0)
        else:
            pass
    return d


def clean_list(lst):
    for i in range(0, len(lst)):
        c = lst[i]
        clean_dict(c)
    return lst
