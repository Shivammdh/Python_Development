import os
try:
    os.removedirs("D:\sh\demo")
    print("complete folder removed sussefully")
except FileNotFoundError:
    print("folder hirerchy does not exists")