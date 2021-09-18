'''the first line contain the number od days N and minTempreture
range(L) and maxTemprature range(R), and next line contain N days
Temprature list. Your task to find list of temprature wich are
 not cover to range L-R where L and R both are Iclusive.

 input: 7 3 6
 2 5 1 8 6 9 4

 output: 2 1 8 9
 '''
d,L,R=input().split()
n=int(d)
minT=int(L)
maxT=int(R)
TempList=list(int(num) for num in input().strip().split())[:n]
ansList=[]
for i in range(n):
    if(not(TempList[i]>=minT and TempList[i]<=maxT)):
        ansList.append(TempList[i])
print(ansList)