try:
    fname=input("enter your file name:")
    rp=open(fname,"r")
    data=rp.readlines()
    
    print("-" * 40)
    for line in data:
        print(line)
    print("-" * 40)
except FileNotFoundError:
    print("file dose not exists")