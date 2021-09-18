import  mysql.connector
try:
	con=mysql.connector.connect(host="localhost",user="root",password="Shivam@0105")
	cur=con.cursor()
	cur.execute("create database html")
	print("data base created--verify in MySQL")
except mysql.connector.DatabaseError as db:
	print("Data base connection Problem:",db)