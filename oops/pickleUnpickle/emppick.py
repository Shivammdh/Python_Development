#emppick.py
import pickle
from employee import Employee
with open("emp.data","ab") as wp:
    empno=int(input("enter how many employee you want:"))
    for i in range(1,empno+1):
        print("="*40)
        print("enter {} employee data".format(i))
        print("="*40)
        eno=int(input("enter employee number:"))
        ename=input("enter employee name:")
        ecomp=input("enter compny name:")
        epos=input("enter employee position:")
        esal=float(input("enter employee sal"))
        so=Employee(eno,ename,ecomp,epos,esal)
        pickle.dump(so,wp)
        print("="*40)
        print("{} employee data saved succefully in file:")
