#vote1.py
class vote:
	#def __init__(self,obj):
	#	self.obj=obj
	#	print(self.obj)

	def getdata(self):
		self.acno=int(input("enter account number:"))
		self.acname=input("enter account hoalder name:")
		self.acbal=float(input("enter balance:"))
		print("shivam")
#main program
obj=vote()
obj.getdata()
#obj.dispdata()
