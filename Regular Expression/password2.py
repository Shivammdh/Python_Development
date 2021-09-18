import re
sp=re.compile(r'[A-Z0-9]+[!@%^&*()_ -+=]+[{"\s"}]')
while(True):
    p=input("enter the password----->")
    if(len(p)>5):
        result=sp.search(p)
        if(result):
            print("valid password")
        else:
            print("not valid password")
    else:
        print("re-enter the password")