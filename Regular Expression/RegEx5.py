import re
#[^a-z] searchs for all except small alphabets
cnt=0
var=re.finditer("[^a-z]","aBcDef12@#$%aBsd!")
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
