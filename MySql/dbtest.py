import  mysql.connector
try:
    con=mysql.connector.connect(host="localhost",user="root",passwd="Shivam@0105")
    if con.is_connected():
        print("Python got connection from MYSQL DB")
    else:
        print("Connection denied")
except mysql.connector.DatabaseError as db:
    print("Data base connection Problem:",db)