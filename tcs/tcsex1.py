s="All the best"
print(s)
s1=""
l=[]
for i in range(len(s)):
	ch=s[i]
	if(ch==" "):
		continue
	elif(ch.isupper()):
		tk=(ord(ch)-65)+1
		l.append(tk)
	else:
		tk=(ord(ch)-97)+1
		l.append(tk)
k=min(l)
for i in range(len(s)):
	ch=s[i]
	if(ch==" "):
		s1+=" "
		continue
	elif(ch.isupper()):
		s1+=chr((ord(ch)+k-65)%26+65)
		
	else:
		s1+=chr((ord(ch)+k-97)%26+97)
print(s1)		