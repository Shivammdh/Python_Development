#InhProg5.py
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
class College(Univ):
	def  getcolldet(self):
		self.colname=input("Enter College Name:")
		self.colloc=input("Enter College Location:")
	def dispcolldet(self):
		print("College details")
		print("-"*50)
		print("College Name:{}".format(self.colname))
		print("College Location:{}".format(self.colloc))
		print("-"*50)
class Student(College):
	def  getstuddet(self):
		self.stno=int(input("Enter Student Number:"))
		self.sname=input("Enter Student Name:")
		self.crs=input("Enter Student Course:")
		self.getcolldet()
		self.getunivdet()
	def dispstuddet(self):
		self.dispunivdet()
		self.dispcolldet()
		print("Student details")
		print("-"*50)
		print("Student Number:{}".format(self.stno))
		print("Student Name:{}".format(self.sname))
		print("Student Course:{}".format(self.crs))
		print("-"*50)

#main program
so=Student()
so.getstuddet()
so.dispstuddet()