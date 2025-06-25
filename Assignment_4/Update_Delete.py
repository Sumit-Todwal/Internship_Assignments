import sqlite3
conn = sqlite3.connect("database.db")
data = conn.execute("Select * from user_details")
for i in data:
    print(i)

conn.execute("delete from user_details where usnm = 'suraj'")

conn.execute("update student set S_mail = 'tushar@gmail.com' where S_name = 'varun'")

datas = conn.execute("Select * from student")
for i in datas:
    print(i)

# All executions are done successfully......
conn.commit()
conn.close()