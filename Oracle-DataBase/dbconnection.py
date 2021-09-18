#dbconnection.py
import cx_Oracle
try:
    kvrcon=cx_Oracle.connect("scott/tiger@localhost/orcl")
    print("python program obtain connection from oracle data base")
except cx_Oracle.DatabaseError as da:
    print("problem is getting the connection")
finally:
    if kvrcon!=None:
        print("db connection close")
        kvrcon.close()

