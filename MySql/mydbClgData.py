import mysql.connector
try:
    mydb=mysql.connector.connect(user="root",host="localhost", password="Shivam@0105")
    mycur=mydb.cursor()
    mycur.execute("create database MyClg")
    print("Database connected succesfully")
except mysql.connector.DatabaseError as db:
    print(db)
