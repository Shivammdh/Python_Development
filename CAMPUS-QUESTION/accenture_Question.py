'''The program accept a string "s" . The string "S" in form of
"a+b=c" .Where a,b and c are positive integer. One part of string
"S" is replaced with a character "X". You are required to replace the
 character "X" With missing digit and return the integral
 representation are same.

 input 1:
 s: 2+15=X

 output:
 17

 input 2:
 22+X=145

 output:
 123

'''
s=input()
s1=s.split("+")
s2=s1[1].split("=")
l1=s1[:1]+s2[:]
if(l1[0]=="X" and (l1[1].isdigit() and l1[2].isdigit())):
    res=abs(int(l1[1])-int(l1[2]))
elif((l1[0].isdigit() and l1[2].isdigit()) and l1[1]=="X"):
    res=abs(int(l1[0])-int(l1[2]))
else:
    res=int(l1[0])+int(l1[1])
print(res)
