l=[3521,2452,1352]
l1=[]
l2=[]
for i in range(len(l)):
    num=l[i]
    largest=0
    smallest=9

    while (num):
        r = num % 10

         # Find the largest digit
        largest = max(r, largest)

         # Find the smallest digit
        smallest = min(r, smallest)
        num = num // 10
    l1.append(largest)
    l2.append(smallest)
print(sum(l1))
print(sum(l2))