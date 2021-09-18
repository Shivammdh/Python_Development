str1=input()
ch=input()
tempstr=""
for i in range(len(str1)):
    if(str1[i]!=ch):
        tempstr+=str1[i]
print(tempstr)