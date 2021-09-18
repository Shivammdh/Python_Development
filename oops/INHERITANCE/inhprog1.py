#InhProg1.py
class Company:
	def  getcompdet(self):
		self.cname="IBM"
		self.cloc="HYD"

class Employee(Company):
	def getempdet(self):
		self.empno=120
		self.ename="Rossum"
		self.sal=23.45
	def dispempdet(self):
		print("---------------------------------------------------------------")
		print("\tEmployee Details:")
		print("---------------------------------------------------------------")
		print("Employee Number: {}".format(self.empno))
		print("Employee Name: {}".format(self.ename))
		print("Employee Salary: {}".format(self.sal))
		print("Company Name: {}".format(self.cname))
		print("Company Location: {}".format(self.cloc))
		print("---------------------------------------------------------------")
#main program
eo=Employee()
eo.getcompdet()
eo.getempdet()
eo.dispempdet()