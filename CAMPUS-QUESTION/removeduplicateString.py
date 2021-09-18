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

n=str(len(l))
print(n)
if(len(str1)>0 and len(str2)>0):
    for j in range(len(str1)):
        score1 += (ord(str1[j]) - ord('a') + 1)
    for k in range(len(str2)):
        score2 += (ord(str2[k]) - ord('a') + 1)
    sc1=str(score1)
    sc2=str(score2)
    print(sc1)
    print(sc2)
    print(n+sc1+sc2)
else:
    for j in range(len(s1)):
        score1 += (ord(s1[j]) - ord('a') + 1)
    for k in range(len(s2)):
        score2 += (ord(s2[k]) - ord('a') + 1)
    sc1 = str(score1)
    sc2 = str(score2)
    print(sc1)
    print(sc2)
    print(sc1 + sc2)

