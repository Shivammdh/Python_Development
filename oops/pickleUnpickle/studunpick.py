#studunpick.py----program--(B)
import pickle
from student import Student
with  open("stud.data","rb") as rp:
	print("------------------------------------------------------")
	print("Student Information:")
	print("------------------------------------------------------")
	while(True):
		try:
			sobj=pickle.load(rp)
			sobj.dispstuddata()
		except EOFError:
			print("------------------------------------------------------")
			break
