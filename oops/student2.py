#student2.py
#Approach2 to add Instance and class level data members through methods

class Student:
	crs="PYTHON"   # here crs is called Class Level Data Member and it is menisoned within								the class definition and before all the methods

	def  setstudentvalues(self):
		self.stno=int(input("Enter Student Number:"))
		self.sname=input("Enter Student Name:")
		self.marks=float(input("Enter Student Marks:"))
		# here we are mensioning Instance DM inside of Instance Method with self
		# self.stno,self.sname and self.marks are called Instance DM
	def dispstudentvalues(self):
		print("Student Number={}".format(self.stno))
		print("Student Name={}".format(self.sname))
		print("Student Marks={}".format(self.marks))
		print("Student Course={}".format(Student.crs))

#main program
s1=Student()
s1.setstudentvalues()
print("--------------------------------------")
s2=Student()
s2.setstudentvalues()
print("------------------------------------------")
print("First Student Values:")
print("------------------------------------------")
s1.dispstudentvalues()
print("------------------------------------------")
print("Second Student Values:")
print("------------------------------------------")
s2.dispstudentvalues()
print("------------------------------------------")


