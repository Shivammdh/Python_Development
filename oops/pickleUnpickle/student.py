#student.py---treated as module
class Student:
	def   __init__(self,sno,sname,smarks,cname):
		self.sno=sno
		self.sname=sname
		self.smarks=smarks
		self.cname=cname

	def dispstuddata(self):
		print("{}\t{}\t{}\t{}".format(self.sno,self.sname,self.smarks,self.cname))
