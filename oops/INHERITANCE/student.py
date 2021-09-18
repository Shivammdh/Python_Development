#student.py---treated as module
from college import College
class Student(College):
	def getstuddet(self):
		self.stno=int(input("Enter Student Number:"))
		self.sname=input("Enter Student Name:")
		self.crs=input("Enter Student Course:")
	def dispstuddet(self):
		print("Student details")
		print("-"*50)
		print("Student Number:{}".format(self.stno))
		print("Student Name:{}".format(self.sname))
		print("Student Course:{}".format(self.crs))
		print("-"*50)