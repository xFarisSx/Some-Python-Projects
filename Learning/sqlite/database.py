import sqlite3



def show_all():
   # connect to database
   conn = sqlite3.connect('customer.db')
   # create a cursor
   c = conn.cursor()
   
   c.execute("SELECT rowid,* FROM aa")
   items = c.fetchall()

   for item in items:
      print(*item)
      
   print("Command executed succesfully...")
   # commit the command
   conn.commit()
   # close connection
   conn.close()

def add_one(first,last,email):
   conn = sqlite3.connect('customer.db')
   c = conn.cursor()
   
   c.execute(f"INSERT INTO aa VALUES (?,?,?)",(first,last,email))
   
   conn.commit()
   conn.close()
   
def delete_one(id):
   conn = sqlite3.connect('customer.db')
   c = conn.cursor()
   
   c.execute("DELETE FROM aa WHERE rowid = ?", id)
   
   conn.commit()
   conn.close()
   
def add_many(list):
   conn = sqlite3.connect('customer.db')
   c = conn.cursor()
   
   c.executemany("INSERT INTO aa VALUES (?,?,?)", (list))
   
   conn.commit()
   conn.close()
   
def email_lookup(email):
   
   conn = sqlite3.connect('customer.db')
   c = conn.cursor()
   
   c.execute("SELECT * FROM aa WHERE email = (?)", (email,))
   
   items = c.fetchall()
   for i in items:
      print(i)
   
   conn.commit()
   conn.close()