import mysql.connector
try:
    db=mysql.connector.connect(host="localhost",user="root",password="Shivam@0105")
    cur=db.cursor()
    cur.execute("create database mydb1")
    print("database created succsefully")
except mysql.connector.DatabaseError as db:
    print(db)
