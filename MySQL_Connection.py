"""
    PYTHON-MYSQL CONNECTION
"""

import mysql.connector as sql

conn = sql.connect(host = 'localhost',
                   user = 'root',
                   password = '0021',
                   database = 'hackermann')

if conn.is_connected(): print("Database 'hackermann' connected succesfully\n")
else: print("Failed to connect to database 'hackermann'!")

cur = conn.cursor()

def createTable(name):
    cur.execute("create table %s (s_id int primary key, s_name char, marks int)" % name)
    conn.commit()
    print("Table", name, "created succesfully")

def addStudent(t_name):
    id = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    cur.execute("insert into %s values(%d, '%s', %d)" % (t_name, id, name, marks))
    conn.commit()
    print("Student added succesfully!")

def displayTable(name):
    cur.execute("select * from %s" % name)
    colnames = [i[0] for i in cur.description]
    print("Table", name, "contents:")
    for i in cur.fetchall():
        print()
        for j in range(len(i)):
            print(colnames[j], "=", i[j])

#addStudent("student")
#createTable("haha")
displayTable("student")
