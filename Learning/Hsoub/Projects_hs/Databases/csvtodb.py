import sqlite3
import csv


con = sqlite3.connect('database.db')
cur = con.cursor()

info = []

file = open('info.csv')
reader = csv.reader(file)

for row in reader:
    info.append(row)

print(info)
cur.execute("""CREATE TABLE if not exists employees (
name VARCHAR(20),
salary INTEGER,
date TEXT
)""")
# for row in info:
#     cur.execute(f"INSERT INTO employees VALUES ('{row[0]}',{row[1]},'{row[2]}')")
cur.executemany("INSERT INTO employees VALUES (?,?,?)", info)
con.commit()
con.close()