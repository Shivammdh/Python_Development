print('Program to form the largest 3-digit number using digits of a given number.\n')
n = 64998420
sn = str(n)
dgtn = []
l=[]

for k in range(len(sn)):
    dgtn += [int(sn[k])]
#dgtn.sort(reverse = True)

temp=dgtn[:2]
s=""
for j in range(len(temp)):
    s+=str(temp[j])
print(s)
t=int(s)
for i in range(1,len(dgtn)):
    if(dgtn[i-1]==dgtn[i]):
        i+=2
    else:
        hd = dgtn[i-1]
        td = dgtn[i]
        i+=2

    max3d = 10 * hd +td
    if(max3d<t):
        max3d=t
# m1=str(max3d)
# for i in range(1,len(max3d)-1):
#     if(max3d[i-1]!=max3d[i]):
#         l.append(max3d)
print(max3d)