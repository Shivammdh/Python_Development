def numtobin(num,*a):
    print(oct(num))

    for i in a:
        print(bin(int(i)))

#l=[x for x in input().split(",")]
n=int(input("enter number which you want oct num:"))
numtobin(n,2,3,4,5,6)