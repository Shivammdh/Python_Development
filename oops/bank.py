#bank.py
class account:
	
	def getaccdet(self):
		self.acno=int(input("enter account number:"))
		self.acname=input("enter account hoalder name:")
		self.acbal=float(input("enter balance:"))
class student:
	def getstuddet(self):
		self.sno=int(input("enter student number:"))
		self.sname=input("enter student name:")
		self.smarks=float(input("enter student marks:"))
		self.sclg=input("enter student college name")
class sinfo:
	@staticmethod
	def dispinfo(obj):
		print("======================================")
		for k,v in obj.__dict__.items():
			print("{}\t{}".format(k,v))
		print("======================================")
#main()
aco=account()
aco.getaccdet()
sinfo.dispinfo(aco)
sto=student()
sto.getstuddet()
sinfo.dispinfo(sto)


