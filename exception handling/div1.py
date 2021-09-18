#div1.py
try:
	a=input("enter first number")
	b=input("enter second number")
	x1=int(a)
	x2=int(b)
	x3=x1/x2
except ValueError:
	print("-"*40)
	print("plese enter only number")
	print("-"*40)
except ZeroDivisionError:
	print("-"*40)
	print("plese take non zero number for denominator")
	print("-"*40)
except IndentationError:
	print("-"*40)
	print("plese take perfact indentation")
	print("-"*40)

else:
	print("-"*40)
	print("first number is=",x1)
	print("second number is=",x2)
	print("Result=",x3)
	print("-"*40)