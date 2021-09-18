''''''

s1=input()
s2=input()
str1=""
str2=""
l=[]
score1 = 0
sc1=""
score2=0
sc2=""
a=list(set(s1)&set(s2))


for i in a:
    l.append(i)
    str1=s1.replace(i,'')
    str2=s2.replace(i, '')
tstr1=""
tstr2=""
for dup1 in str1:
    if str1.count(dup1)>1:
        str1.replace(dup1,"")
    else:
        tstr1+=dup1
for dup2 in str2:
    if str2.count(dup2)>1:
        str2.replace(dup2,"")
    else:
        tstr2+=dup2

print(l)
n=str(len(l))
print(n)
if(len(tstr1)>0 and len(tstr2)>0):
    for j in range(len(tstr1)):
        if tstr1[j].isupper():
            score1 += (ord(tstr1[j]) - ord('A') + 1)
        else:
            score1 += (ord(tstr1[j]) - ord('a') + 1)
    for k in range(len(tstr2)):
        if tstr2[k].isupper():
            score2 += (ord(tstr2[k]) - ord('A') + 1)
        else:
            score2 += (ord(tstr2[k]) - ord('a') + 1)
    sc1=str(score1)
    sc2=str(score2)
    print(sc1)
    print(sc2)
    print(n+sc1+sc2)
else:
    for j in range(len(s1)):
        if s1[j].isupper():
            score1 += (ord(s1[j]) - ord('A') + 1)
        else:
            score1 += (ord(s1[j]) - ord('a') + 1)
    for k in range(len(s2)):
        if s2[k].isupper():
            score2 += (ord(s2[k]) - ord('A') + 1)
        else:
            score2 += (ord(s2[j]) - ord('a') + 1)
    sc1 = str(score1)
    sc2 = str(score2)
    print(sc1)
    print(sc2)
    print(sc1 + sc2)

