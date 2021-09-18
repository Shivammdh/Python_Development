#positionalparam.py
def dispstuddet(sno,sfirstname,slastname,sclg,smarks):
	print("*"*40)
	print("\tSTUDENT DETAIL")
	print("*"*40)
	print("student roll number:{}".format(sno))
	print("student first name:{}".format(sfirstname))
	print("student last name:{}".format(slastname))
	print("student college name:{}".format(sclg))
	print("student marks:{}".format(smarks))
	print("*"*40)
#main progeam
while(True):
	sno=int(input("enter student roll number:"))
	sfname=input("enter student first name:")
	slname=input("enter student last name:")
	sclg=input("enter student college name:")
	smarks=float(input("enter student first name:"))
	dispstuddet(sno,sfname,slname,sclg,smarks)
	ch=int(input("enter 1 of exit and continue to press any key:"))
	if(ch==1):
		print("thanks for using this app")
		exit()

