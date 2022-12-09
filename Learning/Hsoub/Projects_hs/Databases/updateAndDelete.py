import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()

cur.execute('''UPDATE employees SET salary = 600 WHERE name="faris"''')

cur.execute('DELETE FROM employees WHERE name="omar"')

con.commit()
con.close()