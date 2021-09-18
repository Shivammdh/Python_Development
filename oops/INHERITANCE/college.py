#college.py---treated as module
from university import Univ
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