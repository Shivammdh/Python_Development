class Table:
    def getdata(self,n):
        self.n=n
    def setdata(self):
        #self.n=n
        for i in range(1,11):
            print("{}x{}={}".format(self.n,i,self.n*i))
while(True):

    try:

        n=int(input("enter number which table you want to print:"))
        to=Table()
        to.getdata(n)
        to.setdata()
        break
    except ValueError:
        print("you are enter somthing else ..plese enter only number")


