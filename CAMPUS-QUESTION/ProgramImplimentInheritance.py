class first:
    def get(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
class second(first):
    def show(self):
        print(self.firstname)
        print(self.lastname)
obj=second()
obj.get("shivam","sharma")
obj.show()