n1=int(input())
n2=int(input())
max1=max(n1,n2)
i=max1
while(True):
    if(i%n1==0 and i%n2==0):
        break
    i+=max1
print("LCM of {} and {} is :{}".format(n1,n2,i))