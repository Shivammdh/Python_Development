#filetest2.py
with open("sh.data","a+") as fp:
	print("-"*40)
	print("\tfile information")
	print("-"*40)
	print("type of mode:",fp.mode)
	print("type of fp:",type(fp))
	print("is the file are readable:",fp.readable())
	print("is the file are writadable:",fp.writable())
	print("is the file close:",fp.closed)
	print("-"*40)
print("*****out of with... open()... as statement*****")
print("Ia the file closed in out of with...open()...as statement:",fp.closed)