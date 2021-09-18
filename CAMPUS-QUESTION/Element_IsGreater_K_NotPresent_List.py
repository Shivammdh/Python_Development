''' You have a given list which contain N number of integer
values and A number K. Your Task To find the minimum
 grater value of k which is not present in given list.
 input:
 n= 6
 L=2 5 7 9 21 34
 k=20

 Output: 22
 hence min greater value of k is 21 which is present in given list
 so we will discard this min grater value and takes next.
 next min grater value of k is 22 which is not present in given list
 output will be 22.
 '''
import sys

n=int(input())
list1=list(int(num) for num in input().strip().split())[:n]
k=int(input())
while(True):

    if((k not in list1) and (k+1 not in list1)):
        print(k+1)
        break
    elif((k not in list1) and (k+1==list1[n-1])):
        ans=k+1
        print(ans)
        break
    elif((k not in list1) and (k+1 in list1)and (k+1 !=list1[n-1])):
        id=list1.index(k+1)
        for j in range(list1[id],list1[id+1]):
            if(j not in list1):
                print(j)
                sys.exit()
