import sqlite3
conn = sqlite3.connect("database.db")

conn.execute('''
create table User_Details(
usid INTEGER PRIMARY KEY AUTOINCREMENT,
usnm VARCHAR(100),
pass VARCHAR(50),
mobile VARCHAR(15),
email VARCHAR(50)
)
''')

conn.close()