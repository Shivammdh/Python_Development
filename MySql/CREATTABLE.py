#tabcreate.py
import mysql.connector
try:
	con=mysql.connector.connect(host="localhost",
														user="root",
														passwd="Shivam@0105",
														database="html")
	cur=con.cursor()
	tqry="create table tab1(sname varchar(15) not null) "
	cur.execute(tqry)
	print("Table  created in data base --verify in MySQL")
except mysql.connector.DatabaseError as db:
	print("Data base connection Problem:",db)
