s1="program"
str1=""
for i in range(len(s1)):
    if(s1.count(s1[i])>1):
        s1.replace(s1[i],"")

    else:
        str1+=s1[i]
print(str1)