try:
    rp=open("sh.data","r")
    print(rp.tell())
    data = rp.read(6)
    print(data)
    data = rp.read(9)
    print(data)
except FileNotFoundError:
    print("file dose not exist")