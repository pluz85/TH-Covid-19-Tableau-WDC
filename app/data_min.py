import requests as A,json
from app import utility as U
C={'json':'true','Content-Type':'application/json; charset=utf-8'}
D='https://covid19.th-stat.com/api/open/'
def dict(endpoint):
	E=A.get(D+endpoint,headers=C)
	if E.status_code==200:F=E.json();U.c_dict(F);return F
def list(endpoint):
	E=A.get(D+endpoint,headers=C)
	if E.status_code==200:F=E.json()['Data'];U.c_list(F);return json.dumps(F)