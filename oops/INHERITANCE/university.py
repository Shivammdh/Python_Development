#university.py-----treated as module
class Univ(object):
	def getunivdet(self):
		self.univname=input("Enter University Name:")
		self.univloc=input("Enter Univeristy Location:")
	def dispunivdet(self):
		print("-"*50)
		print("University details")
		print("-"*50)
		print("University Name:{}".format(self.univname))
		print("University Location:{}".format(self.univloc))
		print("-"*50)