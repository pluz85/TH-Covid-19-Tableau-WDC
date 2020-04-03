import re
E=str
B='.*<.*?>'
C='\\"'
def D(d):
	for (D,A) in d.items():
		if re.search(B,E(A),0):d[D]=re.sub(B,'',A)
		elif re.search(C,E(A),0):d[D]=re.sub(C,'',A,0)
		else:0
	return d
def A(lst):
	A=lst
	for B in range(0,len(A)):C=A[B];D(C)
	return A