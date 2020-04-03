import requests as C
D={'json':'true','Content-Type':'application/json; charset=utf-8'}
E='https://covid19.th-stat.com/api/open/'
def d_date():
	F=['today','timeline','cases','area'];G=['UpdateDate','LastData'];H=['ข้อมูลประจำวัน','สรุปตามช่วงเวลา','ข้อมูลแต่ละเคส','แจ้งเตือนพื้นที่'];A=[]
	for I in F:
		B=C.get(E+I,headers=D)
		if B.status_code==200:
			for J in G:
				try:K=B.json()[J];A.append(K)
				except KeyError:pass
	L=dict(zip(H,A));return L