import mysql.connector

try:
    con = mysql.connector.connect(host="localhost",
                                  user="root",
                                  passwd="Shivam@0105",
                                  database="pybatch")
    cur = con.cursor()

    while (True):
        try:
            print("--------------------------------------------------")
            stno = int(input("Enter Student Number:"))
            stname = input("Enter Student Name:")
            bname = input("Enter Branch Name:")

            dqry = "insert into student values(%d,'%s','%s') "
            cur.execute(dqry % (stno, stname, bname))
            con.commit()
            print("--------------------------------------------------")
            print("Student Record inserted Successfully...")
            print("--------------------------------------------------")
            ch = input("Do U want to insert another Record (yes / no):")
            if (ch == "no"):
                break
        except ValueError:
            print("Don't enter strs / special symbols/ alphanumerics");

except mysql.connector.DatabaseError as db:
    print("Data Base Problem: ", db)