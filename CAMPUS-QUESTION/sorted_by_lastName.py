names= {'Shivam': 'Sharma','Pyushi': 'Chandra','Neha': 'Lodhi'}

sort_orders = sorted(names.items(), key=lambda x: x[1], reverse=True)
for i in sort_orders:
	print(i[1], i[0])
#here key=lambda x: x[1] a sorting machanism