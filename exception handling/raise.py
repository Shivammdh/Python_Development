#ex1.py
class SkDivisionError(BaseException):pass
def division(x,y):
	if(y==0):
		raise SkDivisionError
	else:
		z=x/y
		return z
try:
	a=int(input("enter first number"))
	b=int(input("enter second number"))
	res=division(a,b)
except SkDivisionError:
	print("don't enter zero for denominator")
except ValueError:
	print("don't enter str,ss,alpha neumeric values")
else:
	print("division={}".format(res))
finally:
	print("i am finally block")

