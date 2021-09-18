#employee.py
class Employee:
    def __init__(self,eno,ename,ecomp,epos,esal):
        self.eno=eno
        self.enmae=ename
        self.ecomp=ecomp
        self.epos=epos
        self.esal=esal
    def dispempdata(self):
        print("{}\t{}\t{}\t{}\t{}".format(self.eno,self.enmae,self.ecomp,self.epos,self.esal))
