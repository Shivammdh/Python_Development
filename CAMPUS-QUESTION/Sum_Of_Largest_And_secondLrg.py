#wiproCode
'''you have given a list of integer number .your task to find
diffrence of sum of the larget and second largest number
 of all the list eliment

input: 3521 2452 1352

output: 5
Explanation:
largest=[5 5 5]
second largest= [3 4 3]
result=(5+5+5)-(3+4+3)=15-10
output: 5
'''
l=[int(x) for x in input().split()]
l1=[]
l2=[]
Largest=0
sec_larg=0
for i in range(len(l)):
    num=l[i]
    largest=0
    Largest = 0
    sec_larg = 0

    while (num>0):
        r = num % 10
        if (Largest < r):
            Sec_Largest = Largest
            Largest = r    #3521
        elif(r >= sec_larg):
            sec_larg = r
        largest = max(r, largest)

        num = num // 10
    l1.append(largest)
    l2.append(sec_larg)
s1=sum(l1)
s2=sum(l2)
print(s1-s2)