'''input:
the input contain integer-barcode,tht represent barcode of the
product.

output:
print a string represent a alphabetic product code

input: 12403

output: bcead
'''
number=int(input())
str1=str(number)
for i in str1:
    print(chr(int(i)+97),end="")