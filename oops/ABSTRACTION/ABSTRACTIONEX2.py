class MyClass:
    __hiddenVariable = 0
    def add(self, increment):
        self.__hiddenVariable += increment
        print(self.__hiddenVariable)



myObject = MyClass()
myObject.add(2)
myObject.add(6)
print((myObject._MyClass__hiddenVariable)+1)
