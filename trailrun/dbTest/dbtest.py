import sqlite3

obj = sqlite3.connect("employee.db")
cur = obj.cursor()

#cur.execute("create table emp(idno integer, name text)")
print("Table created")
cur.execute('''insert into emp(idno, name) values (2654, 'modi')''')
cur.execute('''insert into emp(idno, name) values (2656, 'houdi')''')
cur.execute('''insert into emp(idno, name) values (2658, 'moha')''')
cur.execute('''insert into emp(idno, name) values (2652, 'giri')''')
cur.execute('''insert into emp(idno, name) values (2666, 'vamsi')''')
cur.execute('''select * from emp''')
result = cur.fetchall()
print(result)


obj.close()
