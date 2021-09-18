import os
try:
    os.makedirs("D:\sh\demo\demo1")
    print("folders created sussesfully")
except FileExistsError:
    print("Thise folder is already created")
except FileNotFoundError:
    print("some of the folder is not created ")