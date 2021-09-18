#studpick.py-----------------Program---(A)
import pickle
from student import Student
with  open("stud.data","ab") as wp:
	nos=int(input("How Many student u have to store then in a file:"))
	for i in range(1,nos+1):
		print("------------------------------------------------------")
		print("Enter {} Student Information:".format(i))
		print("------------------------------------------------------")
		stno=int(input("Enter Student Number:"))
		stname=input("Enter Student Name:")
		stmarks=float(input("Enter Student Marks:"))
		stcname=input("Enter Student College Name:")
		so=Student(stno,stname,stmarks,stcname)
		pickle.dump(so,wp)
		print("------------------------------------------------------")
		print("{} student data saved in a file successfully:".format(i))
