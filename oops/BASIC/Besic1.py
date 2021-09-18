class Shivam:
    def detail(self,name,phone,clg):
        print(name)
        print(phone)
        print(clg)
    def shivamdetails(self,name,phone):
        clg="oist"
        phone=1234567890
        print("-"*40)
        print("Call by Object Name...")
        print("-" * 40)
        obj.detail(name,phone,clg)
        print("-" * 40)
        print("Call by class Name...")
        print("-" * 40)
        Shivam().detail(name, phone, clg)
        print("-" * 40)
        print("Call by self Name...")
        print("-" * 40)
        self.detail(name, phone, clg)
        print("-" * 40)

#Shivam().shivamdetails("shivam",9589576566)
obj=Shivam()
obj.shivamdetails("shivam",9589576566)