class Myclass:
    def add(self,a,b):
        return a+b

    def add(self,a,b):
        return a+b
a=int(input())
b=int(input())
str1=input()
str2=input()
obj=Myclass()
addres=obj.add(a,b)
subres=obj.add(str1,str2)
print(addres)
print(subres)

