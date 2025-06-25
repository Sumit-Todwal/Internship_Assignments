import sqlite3
conn = sqlite3.connect("database.db")
conn.execute('''
create table Employee(
E_id integer primary key autoincrement,
e_name varchar(20),
e_mail varchar(20),
e_mobile varchar(15)
)
''')
conn.close()