import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()

command = """CREATE TABLE if not exists students (
firstName VARCHAR(20),
lastName VARCHAR(20),
age INTEGER)"""

cur.execute(command)

cur.execute('INSERT INTO students VALUES ("faris", "hasan", 23)')
cur.execute('INSERT INTO students VALUES ("hasan", "faris", 34)')
cur.execute('INSERT INTO students VALUES ("omar", "ibrahim", 10)')

con.commit()

con.close()