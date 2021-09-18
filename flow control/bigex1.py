#wap which will decided biggest of three number
#bigex1.py
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
#logic
if((a==b)and(b==c)and(c==a)):
	print("All value are equal")
else:

	big=a
	if(b>big):
		big=b
	if(c>big):
		big=c
	print("biggest is:",big)