num = input("Enter the number : ")
sum=0
if len(num) == 2:
    print(f"Largest digit is : {num}")
    exit(0)
elif len(num) < 2:
    print(-1)
    exit(0)

maxans = int((num[0].replace("0", "")))*10 + int((num[1].replace("0", "")))
prev = maxans
for i in range(2, 6):
    cur = (prev%10)*10 + int((num[i].replace("0", "")))
    temp=str(cur)
    for j in range(1,len(temp)):
        if(ord(temp[j-1])==ord(temp[j])):
            continue
            i+=1
        else:
            temp1=int(temp)
            maxans = max(maxans,temp1)
            prev = temp1

print(f"The Largest num = : {maxans}")