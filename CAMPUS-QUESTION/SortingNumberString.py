'''
you have given a string your task to sort the string and print them
in following way:
Case:1
input:- 1,2,4,2
output:- 1,2,2,4

case:2
input: 7,8,1,3,2
output: 1,2,3,7,8
'''
s=input()
l=s.split(",")
l.sort()
ans=",".join(l)
print(ans)