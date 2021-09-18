import os
try:
    os.rmdir("D:\sh\demo\demo1")
    print("folder removed sussefully")
except FileNotFoundError:
    print("fttempting to remove a folder, where it does not exists")
except OSError:
    print("ttempting to remove the folder, where it contains files or sub folders")