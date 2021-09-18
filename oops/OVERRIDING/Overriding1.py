class Teacher:
    def advise(self):
        print("-"*40)
        print("teacher advice")
        print("read 2 hr")
        print("prectice 2 hr")
        print("-"*40)
class LezyStudent(Teacher):
    def advise(self):
        print("Lezy Student advise")
        print("Reding 20 mint ")
        print("no prectice")
        super().advise()
class PerfectSudent(Teacher):
    def advise(self):
        print("perfect student advise")
        print("read 4 hr")
        print("prectice 3hr")
        super().advise()
lo=LezyStudent()
lo.advise()
print("-"*40)
po=PerfectSudent()
po.advise()
