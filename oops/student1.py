#student1.py
#-Approach1 to add Instance and class level data members through object name

class Student:pass



#main program
Student.crs="PYTHON"   # here crs is called Class Level Data Member
s1=Student()    # first object created
print("id of s1=",id(s1))
s1.stno=100
s1.sname="RS"
s1.marks=34.56
print("--------------------------------")
s2=Student()    # second object created
print("id of s2=",id(s2))
s2.stno=101
s2.sname="DR"
s2.marks=44.56
print("--------------------------------------------")
print("First Student Values:")
print("--------------------------------------------")
print("Student Number={}".format(s1.stno))
print("Student Name={}".format(s1.sname))
print("Student Marks={}".format(s1.marks))
print("Student Course={}".format(Student.crs))
print("Student another Course={}".format(s1.crs))
print("--------------------------------------------")
print("Second Student Values:")
print("--------------------------------------------")
print("Student Number={}".format(s2.stno))
print("Student Name={}".format(s2.sname))
print("Student Marks={}".format(s2.marks))
print("Student Course={}".format(Student.crs))
print("--------------------------------------------")