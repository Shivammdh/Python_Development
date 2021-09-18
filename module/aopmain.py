from dip import dipaop
from aop import*
import sys
while(True):
	dipaop()
	ch=int(input("ENTER YOUR CHOICE:"))
	if(ch==1):
		addition()
	elif(ch==2):
		substraction()
	elif(ch==2):
		substraction()
	elif(ch==3):
		multiplication()
	elif(ch==4):
		division()
	elif(ch==5):
		expo()
	elif(ch==6):
		print("THANKS USER FOR USING THIS APP!!")
		sys.exit()
	else:
		print("BE-CAREFUL...YOU SELECT WRONG CHOICE..PLESE RE-ENTER RIGHT CHOICE")
