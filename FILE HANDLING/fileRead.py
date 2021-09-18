try:
    rp=open("sh.data","r")
    data=rp.read()
    print(data)
except FileNotFoundError:
    print("file dose not exist")