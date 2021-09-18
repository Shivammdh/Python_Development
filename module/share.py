#share.py
sv={"IT":1020,"PS":33000,"IS":34500}
def dispshare():
	print("-"*40)
	print("\tsharename\tsharevalue")
	print("-"*40)
	for k,v in sv.items():
		print("\t{}\t\t{}".format(k,v))
	print("-"*40)