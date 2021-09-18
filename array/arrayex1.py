from array import *
vals=array('i',[1,2,3,4,5])
#vals1=array('i',[1,2,3.5,4,5])-->TypeError: integer argument expected, got float
vals.reverse()#[5,4,3,2,1]
print(vals,type(vals))

for i in range(5):
    print(vals[i])
