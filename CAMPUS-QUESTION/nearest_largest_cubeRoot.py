'''You have given a list of products price. your task is to
calculate the total price of product. If total price of products
is a perfact cube then program will be return "YES" Otherwise
 return diffrence B/W largest nearest cube of given products price
 and total of products price

 input:
 6
 60 7 8 10 250 730
 output: 266

 explainetion
 ------------------------------------------------------------------
 total products price=60+7+8+10+250+730=1065 ,which is not a perfect
 cube the nearest largest perfect cube of its number is 1331
 answer=1331-1065=266

 input:
 5
 60 891 520 213 44
 output: YES

Explenation
--------------------------------------------------------------------
total product price=60+891+520+213+44=1728, Which is a perfect cube
then it will return "YES".
 '''

import  math
n=int(input())
Products_Price=list(int(num) for num in input().strip().split())[:n]
sum=sum(Products_Price)

if(round(sum** (1 / 3)) ** 3 == sum):
    print("YES")
else:
    cubert = sum ** (1 / 3)
    secCub = math.ceil(cubert)
    largCube = secCub ** 3
    result =largCube-sum
    print(result)