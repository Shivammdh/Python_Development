import mysql.connector

try:
    con = mysql.connector.connect(host="localhost",
                                  user="root",
                                  passwd="Shivam@0105",
                                  database="html")
    cur = con.cursor()

    while (True):
        try:
            print("--------------------------------------------------")
            num1=int(input())
            dqry = "insert into tab1 values(%d) "
            cur.execute(dqry % (num1))
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