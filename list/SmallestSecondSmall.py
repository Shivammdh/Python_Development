l=[int(x) for x in input().split()]
s1=set(l)
l1=list(s1)
l1.sort()
m1=min(l1)
m2=l1.index(m1)
m3=l1[m2+1]
print(m1,m3)