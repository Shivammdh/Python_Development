try:
    rp=open("sh.data","r")
    data=rp.readline()
    print(data)
    data = rp.readline()
    print(data)
    data = rp.readline()
    print(data)
except FileNotFoundError:
    print("file dose note exist")