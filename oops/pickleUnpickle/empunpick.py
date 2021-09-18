#empunpick.py
import pickle
from employee import Employee
with open("emp.data","rb") as rp:
    print("="*40)
    print("Employee Information")
    print("=" * 40)
    print("eno\tename\tecomp\tepos\tesal")
    print("-"*40)
    while(True):
        try:
            eo=pickle.load(rp)
            eo.dispempdata()
        except EOFError:
            print("="*40)
            break