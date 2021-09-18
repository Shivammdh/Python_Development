#listcomp.py
n=int(input())
l=[]
for i in range(n):
	sname=input()
	smarks=float(input())
	l.append([sname,smarks])
sorted_scor=sorted(list(set([x[1] for x in l])))
s_low=sorted_scor[1]
lflist=[]
for s in l:
	if s_low==s[1]:
		lflist.append(s[0])
for stud in sorted(lflist):
	print(stud)
