import mysql.connector
try:
    mydb=mysql.connector.connect(user="root",host="localhost", password="Shivam@0105")
    mycur=mydb.cursor()
    mycur.execute("show databases")
    for x in mycur:
        print(x)
except mysql.connector.DatabaseError as db:
    print(db)
