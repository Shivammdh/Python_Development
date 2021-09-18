class Factorial:
    def __init__(self,n):
        self.n = n
        fact = 1
        for i in range(1,n+1):
            fact*= i
        print(fact)
try:
    n=int(input("enter a number:"))
    obj=Factorial(5)
except ValueError:
     print("please enter integer value...")