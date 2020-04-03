from flask import current_app as A,send_file as D
import json,pandas as B,io,datetime as C
G=True
def E(endpoint,*B,**C):D=A.view_functions[endpoint];E=D(*B,**C);F=json.loads(E);return F
def F(data,endpoint):D=B.DataFrame(data);A=io.BytesIO();C=B.ExcelWriter(A,engine='xlsxwriter');D.to_excel(C,sheet_name=endpoint,index=False,header=G,encoding='utf-8');C.save();A.getvalue();A.seek(0);return A
def dl(endpoint):A=endpoint;B=(C.date.today()+C.timedelta(hours=11)).strftime('%d%m%Y');H=A+'_'+B;I=E('api.'+A);J=F(I,A);return D(J,attachment_filename=H+'.xlsx',as_attachment=G)