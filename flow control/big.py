#wap which will decided biggest of three number
#big.py
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
#logic
big=a
if(b>big):
	big=b
if(c>big):
	big=c
print("biggest is:",big)