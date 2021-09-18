#evenodd.py
l=[int(x) for x in input().split(",")]
print("origenal eliment in list:",l)
pe=list(filter(lambda v:True if(v%2==0) else False,l))
po=list(filter(lambda v:True if(v%2==1) else False,l))
print(max(pe))
print(max(po))