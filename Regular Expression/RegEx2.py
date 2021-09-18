import re
s1="python"
s2="python is opps lang. python is also pop lang"
cnt=0
var=re.finditer(s1,s2)
print(var)
print(type(var))
print("========================================")
print("start\tend\tstring")
for i in var:
    cnt+=1

    print("{}\t\t{}\t{}".format(i.start(),i.end(),i.group()))
else:
    print("="*40)
    print("total occurence is",cnt)
    print("=" * 40)

