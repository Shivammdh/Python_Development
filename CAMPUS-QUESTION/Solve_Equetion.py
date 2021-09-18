'''Your math teacher have given you to a problem equation.
Equetion is equ=(1^n+2^n+3^n+4^n)%5. solve this equestion in programming
 where n is a value which is given that.
 input:
 testCase: 3
 n=8 6 7

 output: 4 0 0
 '''
t=int(input())
while(t):
    n=int(input())
    l=list(int(x) for x in input().strip().split())[:n]
    l1=[]
    for i in range(n):

        equ=(1**l[i])+(2**l[i])+(3**l[i])+(4**l[i])
        ans=equ%5
        l1.append(ans)
    print(l1)
    t-=1
