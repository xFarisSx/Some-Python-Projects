import sqlite3, sys

message = """
"a" => Add New Task
"d" => Delete a Task
"s" => Show All Tasks
"u" => Update a Task
"q" => Quit The App
Please choose an option:
"""

user_input = input(message).strip().lower()
commands_list = ["a", "d", "s", "u", "q"]
user_id = 1

try:
    con = sqlite3.connect("todoAPP.db")
    cur = con.cursor()
except:
    print("connection error")
finally:
    if(con):
        command = """CREATE TABLE if not exists tasks (user_id INTEGER, task_name VARCHAR(20), description TEXT)"""
        cur.execute(command)
        def show_tasks():
            cur.execute(f"""SELECT * FROM tasks WHERE user_id='{user_id}'""")
            all_tasks = cur.fetchall()

            print(f"You have {len(all_tasks)} tasks")
            if len(all_tasks) > 0:
                print("""Task Name   |   Description
----------------------------""")
                for row in all_tasks:
                    print(f"{row[1]}   |   {row[2]}")
            con.commit()

        def add_task():
            task_name = input("Task Name: ").strip()
            des = input("Task Description: ").strip()

            cur.execute(f"INSERT INTO tasks VALUES ('{user_id}', '{task_name}', '{des}')")
            con.commit()


        def delete_task():
            task_name = input("Task Name: ").strip()
            cur.execute(f"DELETE FROM tasks WHERE task_name='{task_name}' and user_id='{user_id}'")
            con.commit()

        def update_task():
            task_name = input("Task Name: ").strip()
            cur.execute(f"SELECT * FROM tasks WHERE task_name='{task_name}' AND user_id='{user_id}'")
            results = cur.fetchall()

            if not results:
                print("There is no task with this name")
            else:
                modify = input("Des or name: ")
                if modify == "des":
                    des = input("New Des: ")
                    cur.execute(f"""UPDATE tasks SET description='{des}' WHERE task_name='{task_name}' AND user_id='{user_id}""")
                    con.commit()
                else:
                    new_name = input("New Name: ")
                    cur.execute(f"""UPDATE tasks SET task_name='{new_name}' WHERE task_name='{task_name}' AND user_id='{user_id}'""")
                    con.commit()


        def end_app():
            sys.exit()


        if user_input in commands_list:
            if user_input == "s":
                show_tasks()
            elif user_input == "a":
                add_task()
            elif user_input == "d":
                delete_task()
            elif user_input == "u":
                update_task()
            elif user_input == "q":
                end_app()

        else:
            print("Sorry this command is not found")


    con.close()