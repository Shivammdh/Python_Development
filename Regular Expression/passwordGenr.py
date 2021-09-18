import re
#[A-Z] searchs for all alphabets(capital,small) and digits

s=input("enter password:")

if re.search("[A-Za-z0-9@#$%^&+=]",s):
    print("Valid")
else:
    print("invalid")
# print(var)
# print(type(var))
# print("========================================")
# print("start\tend\tstring")
# for i in var:
#     cnt+=1
#
#     print("{}\t\t{}\t{}".format(i.start(),i.end(),i.group()))
# else:
#     print("="*40)
#     print("total occurence is",cnt)
#     print("=" * 40)
