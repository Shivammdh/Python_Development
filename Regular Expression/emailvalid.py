import re
reg='[a-z0-9]+[@]\w+[.]\w{3}$'
email=input("enter email:")
if(re.search(reg,email)):
    print("valid email")
else:
    print("email not valid")
