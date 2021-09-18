l= int(input())
n = int(input())
i = 0
while i < n:
    wh = (input().split())
    w = int(wh[0])
    h = int(wh[1])
    if w < l or h < l:
        print('UPLOAD ANOTHER')
    else:
        if w == h and (w >= l and h >= l) :
          print('ACCEPTED')  
        else:
            print('CROP IT')

    i+=1