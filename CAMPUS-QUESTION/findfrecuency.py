s=input()
sum=0
s1=s.split("+")

s2=s1[1].split("=")


l1=s1[:1]+s2[:]
if(l1[0].isdigit() and l1[1].isdigit()):
    res=int(l1[0])+int(l1[1])
    print(res)
elif(l1[0].isdigit() and l1[1]=="X"):
    res1=abs(int(l1[0])-int(l1[2]))
    print(res1)





for i in range(len(l1)):
    if(l1[i].isdigit()):
        a=l1[i]

print(sum)
