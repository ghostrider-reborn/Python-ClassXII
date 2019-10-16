"""
    PYTHON-MYSQL CONNECTION
"""

import sys, mysql.connector as sql

# Initialize connection to local database 'hackermann'
conn = sql.connect(host = 'localhost',
                   user = 'root',
                   password = '0021',
                   database = 'hackermann')

if conn.is_connected():
    print("DB connected succesfully!")
    cur = conn.cursor()
else:
    print("Connecting to database failed!")
    sys.exit()

def createStudentTable(name):
    ''' Create pre-defined table named 'student' '''
    cur.execute("create table %s (s_id int primary key, s_name char, marks int)" % name)
    conn.commit()
    print("Table", name, "created succesfully")

def addRow(t_name):
    ''' Add a row in any generic table '''
    cur.execute('desc %s' % t_name)
    colnames = [i[0] for i in cur.fetchall()]
    values = [t_name]
    for col in colnames: values.append(input("Enter '%s' value: " % col))

    cur.execute("insert into %s values(%s, '%s', %s)" % tuple(values))
    conn.commit()
    print("Row added succesfully!")

def display(data):
    ''' Display given fetchall() data '''
    colnames = [i[0] for i in cur.description]
    for i in data:
        print()
        for j in range(len(i)):
            print(colnames[j], "value:", i[j])

def displayTable(name):
    ''' Display entire contents of a specified table '''
    cur.execute("select * from %s" % name)
    colnames = [i[0] for i in cur.description]
    print("Table", name, "contents:")
    display(cur.fetchall())

#createStudentTable("haha")
#addRow("student")
displayTable("student")
