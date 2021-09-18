srcfile=input("enter source file:")
try:
    with open(srcfile,"r") as rp:
        destfile=input("enter destinetion file:")
        with open(destfile,"a") as wp:
            srcfile=rp.read()
            wp.write(srcfile)
            print("source file data copied into destinetion file")
except FileNotFoundError:
    print("source file dose note exists")