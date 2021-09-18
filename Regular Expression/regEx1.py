import re
s1="python"
s2="python is opps lang. python is also pop lang"
var=re.finditer(s1,s2)
print(var)
print(type(var))
for i in var:
    print("{}\t{}\t{}".format(i.start(),i.end(),i.group()))