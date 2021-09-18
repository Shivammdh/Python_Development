class Solution:
    def countBits(self, N, A):
        ans=0
        for i in range(0,32):
            count=0
            for j in range(0,N):
                if(A[j] & (1<<i)):
                    count+=1
            ans += (count * (N - count) * 2)
        return ans%1000000007
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        A=input().split()
        for it in range(N):
            A[it]=int(A[it])
        ob=Solution()
        print(ob.countBits(A,N))