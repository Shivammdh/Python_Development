import re
#[A-Z] searchs for all except alphabets(capital,small)
cnt=0
var=re.finditer("[^A-Za-z]","aBcDef12@#$%a0Bsd3xX!")
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
