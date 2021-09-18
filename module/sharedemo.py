#sharedemo.py
import share,time,importlib
share.dispshare()
time.sleep(30)
print("*"*40)
importlib.reload(share)
share.dispshare()