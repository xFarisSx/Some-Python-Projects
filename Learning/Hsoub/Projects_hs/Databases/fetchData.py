import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()

cur.execute("SELECT * FROM employees WHERE salary > 100")
# print(cur.fetchall())
# print(cur.fetchone())
print(cur.fetchmany(3))

answer = cur.fetchall()
for i in answer:
    print(i)