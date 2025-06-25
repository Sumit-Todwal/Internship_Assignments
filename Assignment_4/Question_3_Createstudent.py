import sqlite3
conn = sqlite3.connect("database.db")

conn.execute('''
create table Student(
S_id Integer Primary Key AUTOINCREMENT,
S_name VARCHAR(20),
s_MAIL VARCHAR(20),
s_MOBILE VARCHAR(20)
)
''')
conn.close()