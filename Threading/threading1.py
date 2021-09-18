from threading import *
from time import sleep
class s1(Thread):
    def run(self):
        for i in range(5):

            print("hii")
            sleep(1)
class s2(Thread):
    def run(self):
        for i in range(5):

            print("hello")
            sleep(1)

#main program
o1=s1()
o2=s2()
o1.start()
sleep(0.2)
o2.start()
o1.join()
o2.join()
print("bye")