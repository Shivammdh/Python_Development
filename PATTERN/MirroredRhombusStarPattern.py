row=int(input())
col=int(input())
for i in range(row-1,-1,-1):
    for j in range(i):
        print(" ",end="")
    for k in range(col):
        print("*",end="")
    print("")