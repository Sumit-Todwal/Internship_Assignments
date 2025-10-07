import sqlite3
import os
from flask import g

# DB_PATH = os.path.join("instance","database.db")

def get_connection():
    conn = sqlite3.connect("instance/database.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    print(os.path.abspath("instance/database.db"))
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
                   )
''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS devices(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            device_name TEXT NOT NULL,
            Location TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE             
                   )
''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS energy_data(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id INTEGER NOT NULL,
            timestamp TEXT NOT NULL,
            current REAL NOT NULL,
            voltage REAL NOT NULL,
            FOREIGN KEY (device_id) REFERENCES devices(id) ON DELETE CASCADE
            )
''')
    conn.commit()
    conn.close()