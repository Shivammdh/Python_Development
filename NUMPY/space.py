#space.py
import numpy as np
import sys
l1=[10,20,30,-45,20,30,40,50,60,40,60,90,70,34,567,1234,56,10,20,30,-45,20,30,40,50,60,40,60,90,70,34,567,1234,56,10,20,30,-45,20,30,40,50,60,40,60,90,70,34,567,1234,56]
a=np.array([10,20,30,-45,20,30,40,50,60,40,60,90,70,34,567,1234,56,10,20,30,-45,20,30,40,50,60,40,60,90,70,34,567,1234,56,10,20,30,-45,20,30,40,50,60,40,60,90,70,34,567,1234,56])
print("-----------------------------------------------------------")
print("memory space taken l1 internally={}".format(sys.getsizeof(l1)))
print("memory space taken ndarray object internally={}".format(sys.getsizeof(a)))
print("-----------------------------------------------------------")