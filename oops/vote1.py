#vote1.py
class vote:
	def __init__(self,obj):
		self.obj=obj
		print(self.obj)

	def getdata(self):
		while(True):
			self.age=int(input("enter citizen age:"))
			if((self.age>=18) and (self.age<100)):
				return "YOU ARE ELIGIBLE TO VOTE"
				break
#main program
obj=vote()
res=obj.getdata()
v=vote(res)

