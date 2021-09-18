#aop.py
def readvalue(op):
	print("enter two values for {}".format(op))
	a=float(input())
	b=float(input())
	return a,b
#main
def addition():
	a,b=readvalue("ADDITION")
	print("sum of {} and {}={}".format(a,b,a+b))

def substraction():
	a,b=readvalue("SUBSTRACTION")
	print("suB of {} and {}={}".format(a,b,a-b))

def multiplication():
	a,b=readvalue("MULTIPLICATION")
	print("MUL of {} and {}={}".format(a,b,a*b))

def division():
	a,b=readvalue("DIVISION")
	print("DIV of {} and {}={}".format(a,b,a/b))

def expo():
	a,b=readvalue("EXPONENTIATION")
	print("{} power of {}={}".format(a,b,a**b))