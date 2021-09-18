try:
    fname = input("enter file name:")
    with open(fname,"a") as wp:
        print("multiple line text...to end press 'stop'")
        print("-"*40)
        while(True):
            mldata=input()
            if(mldata!="stop"):
                wp.write(mldata+"\n")
            else:
                break
        print("-"*40)
        print("data written file verify...")
        print("-"*40)
except FileNotFoundError:
    print("given file is not exist")


