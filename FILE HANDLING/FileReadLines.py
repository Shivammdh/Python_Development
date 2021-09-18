try:
    rp=open("sh.data","r")
    data=rp.readlines()
    print("-"*40)
    print("Print the data in list form")
    print("-" * 40)
    print(data)
    print("-" * 40)
    print("print the data use of loop")
    print("-" * 40)
    for line in data:
        print(line)
    print("-" * 40)
except FileNotFoundError:
    print("file dose not exists")