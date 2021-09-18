'''you have a given string sepreted by space .your task to find
the length of last word of given string
input: i am a good developer
output: 9

explanation:
--------------------------------------------------------------=
in this case last word of string is developer and length of word
developer is is 9. hence answe will be 9.
'''
string=input()
lstring=string.split()
n=len(lstring)
result=len(lstring[n-1])
print(result)
