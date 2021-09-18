#chek given input is a digit or not
#if_elif_else.py
try:

	d=int(input("enter any digit:"))
	if(d==0):
		print("you entered:",d)
	elif(d==1):
		print("you entered:",d)
	elif(d==3):
		print("you entered:",d)
	elif(d==4):
		print("you entered:",d)
	elif(d==5):
		print("you entered:",d)
	elif(d==6):
		print("you entered:",d)
	elif(d==7):
		print("you entered:",d)
	elif(d==8):
		print("you entered:",d)
	elif(d==9):
		print("you entered:",d)
	elif(len(str(d))>1):
		print("you entered {} which is not a digit...+iv/-iv".format(d))
	
except ValueError:
	print("plese enter only digit")