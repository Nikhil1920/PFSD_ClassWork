import sqlite3

obj = sqlite3.connect("studentDetails.db")
cur = obj.cursor()

# cur.execute(
#     "create table Studentdetails(entryid integer, idno integer, name text, marks integer)")
print("Studentdetails Table created")

cur.execute(
    "insert into Studentdetails(entryid, idno, name, marks) values (1, 190031025, 'Ravi', 58)")
cur.execute(
    "insert into Studentdetails(entryid, idno, name, marks) values (2, 190031025, 'Ravi', 58)")
cur.execute(
    "insert into Studentdetails(entryid, idno, name, marks) values (3, 190031025, 'Ravi', 58)")
cur.execute(
    "insert into Studentdetails(entryid, idno, name, marks) values (4, 190031025, 'Ravi', 54)")
cur.execute(
    "insert into Studentdetails(entryid, idno, name, marks) values (5, 190031025, 'Ravi', 58)")

cur.execute('''select * from Studentdetails''')
result = cur.fetchall()
print(result)

cur.execute('''DELETE FROM Studentdetails
WHERE entryid=3''')

print("Deteted third column data")
cur.execute('''select * from Studentdetails''')
result = cur.fetchall()
print(result)

cur.execute('''
UPDATE Studentdetails
SET marks = 66
WHERE entryid=4
''')

print("Updated the fourth column data")
cur.execute('''select * from Studentdetails''')
result = cur.fetchall()
print(result)

obj.close()
