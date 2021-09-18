''''''
l=[int(x) for x in input().split()]
sum=0
for i in range(len(l)):
    if(i%2==0):
        sum=sum+l[i]
print(sum)