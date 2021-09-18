#filetest1.py
try:
	fp=open("hyd.data","w")
	print("-"*40)
	print("\tfile information")
	print("-"*40)
	print("thpe of mode",fp.mode)
	print("type of fp",type(fp))
	print("is the file are readable",fp.readable())
	print("is the file are writadable",fp.writable())
	print("is the file close",fp.closed)
	print("-"*40)

except Exception as e:
	print(e)
finally:
	if fp!=None:
		print("File close succesfully.........")
		fp.close()
		print("is the file close in finally block=",fp.closed)
	else:
		print("file not at opened")
