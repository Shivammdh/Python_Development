def Validate(n):
    if(n<5):
        return 0
def duplicate(a,n):
    for i in range(n):
        if(a.count(a[i])>1):
            return 1
def team_devide(arr1,n):
    fb=[]
    bb=[]
    for i in range(n):
        if(arr1[i]%2==0):
            fb.append(arr1[i])
        else:
            bb.append(arr1[i])
    print("list of employee in football team are:",fb)
    print("list of employee in basketball team are:", bb)
def main():
    arr1=[]
    n=int(input())
    for y in range(0,n):
        num=int(input())
        arr1.append(num)
    if Validate(n)==0:
        print("number of employee must be greater than 5")
    elif duplicate(arr1,n)==1:
        print("duplicate are present")
    else:
        team_devide(arr1, n)
main()