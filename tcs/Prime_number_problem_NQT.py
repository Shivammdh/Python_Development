n=int(input())
m=int(input())
l=[]
count=0
for i in range(n,m+1):
    if i>1:
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            l.append(i)
print(l)
for k in range(0,len(l)):
    for num in range(k+1,len(l)):
        if(abs(l[k]-l[num])==6):
            count+=1
print(count)
