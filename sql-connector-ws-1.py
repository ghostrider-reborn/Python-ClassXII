import sys, mysql.connector as sql

# Initialize connection to local database 'hackermann'
conn = sql.connect(host = 'localhost',
                   user = 'root',
                   password = '0021',
                   database = 'adithya')

if conn.is_connected():
    print("DB connected succesfully!")
    cur = conn.cursor()
else:
    print("Connecting to database failed!")
    sys.exit()

cur = conn.cursor()

def printResult():
    print(cur.column_names)
    for row in cur.fetchall(): print(row)

# query 1
print("\nQuery 1 result:")
cur.execute("select agency, sum(package_amt) as 'total earnings' from tourist group by agency")
printResult()

# query 2:
print("\nQuery 2 result:")
cur.execute("select t.name as 'tname', p.name as 'pname' from tourist t, places p where t.tcode = p.T_code")
printResult()

print("\nQuery 3 result:")
cur.execute("select count(name) from places where name like 'A%'")
printResult()

print("\nQuery 4 result:")
cur.execute("select max(package_amt), min(package_amt), sum(package_amt) from tourist")
printResult()

print("\nQuery 5 result:")
cur.execute("select * from tourist where age in (21, 23, 26)")
printResult()

print("\nQuery 6 result:")
cur.execute("select t.name as 'tname', t.package_amt, p.name as 'pname' from tourist t, places p where t.tcode = p.t_code and t.name in ('Hardeep', 'Kavita', 'Medha')")
printResult()

print("\nQuery 7 result:")
cur.execute("select * from tourist order by name desc")
printResult()

print("\nQuery 8 result:")
cur.execute("update tourist set package_amt = package_amt*1.1")
cur.execute("select * from tourist")
printResult()
conn.commit()
