srcfile=input("enter source file name:")
try:
    with open(srcfile,"r") as rp:
        destfile=input("enter destination file:")
        with open(destfile,"a") as wp:
            srcdata=rp.read()
            wp.write(srcdata)
            print("source file data copy......")
except FileNotFoundError:
    print("file does not exites")