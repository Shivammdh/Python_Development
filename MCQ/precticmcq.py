values = [1,1,2,2,3, 2, 3, 4]
numbers = set(values)

def checknums(num):
	if num in values:
		return True
	else:
		return False

for i in filter(checknums, numbers):
	print(i)
