#vote.py
class vote:
	def __init__(self):
		while(True):
			self.age=int(input("enter citizen age:"))
			if((self.age>=18) and (self.age<100)):
				print("YOU ARE ELIGIBLE TO VOTE")
				break
#main program
v=vote()
