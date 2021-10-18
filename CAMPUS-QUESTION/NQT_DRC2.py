'''
You have given a Item Number list is, item=[101,102,103,104],item name
iname=["Milk","apple","Ghee","Oil"], Item Price according to
item number is price=[42,45,48,46],and item stock is per item no.
is stock=[10,14,17,16].
User give 2 input first item number and quantity of item, Your Task
is to calculate the total price of item number as per item quantity
and also reduce the quantity of item in item stock and print them

if item stock is less than item quantity then print "NO STOCK" and
also print original quantity of item.

input-1: 101
         4
outpur:
        168.0 INR
        6 LEFT

INPUT-2:
        104
        20
OUTPUT:
        NO STOCK
        16 LEFT

'''

item=[101,102,103,104]
iname=["Milk","Graps","Ghee","Oil"]
price=[42,45,48,46]
stock=[10,14,17,16]
item_no=int(input())
iquant=int(input())
f=0
p1=0.0
q1=0
s1=""
for i in range(len(item)):
    if(item_no==item[i]):
        if(iquant<=stock[i]):
            p1=float(price[i]*iquant)
            q1=stock[i]-iquant
            f=1
        else:
            s1="NO STOCK"
            q1=stock[i]
if(f==0):
    print(f"{s1}")
    print(f"{q1} LEFT")
else:
    print(f"{p1} INR")
    print(f"{q1} LEFT")
