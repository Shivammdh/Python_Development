#InhProg2.py
class Company:
	def  getcompdet(self):
		self.cname="IBM"
		self.cloc="HYD"

class Food:
	def getfooddet(self):
		self.avfood="Biryani"
		self.drink="Apple Juice"

class Employee(Company, Food):
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
		print("Today Employee Food: {}".format(self.avfood))
		print("Today Employee Drink: {}".format(self.drink))
		print("Company Name: {}".format(self.cname))
		print("Company Location: {}".format(self.cloc))
		print("---------------------------------------------------------------")
#main program
eo=Employee()
eo.getcompdet()
eo.getfooddet()
eo.getempdet()
eo.dispempdet()