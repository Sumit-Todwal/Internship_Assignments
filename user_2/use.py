import sqlite3
import hashlib
import getpass
from abc import ABC, abstractmethod


# --------------------- Database Handler ---------------------
class IDatabaseService(ABC):
    @abstractmethod
    def connect(self): pass

    @abstractmethod
    def execute(self, query, params=()): pass

    @abstractmethod
    def fetchone(self): pass

    @abstractmethod
    def fetchall(self): pass

    @abstractmethod
    def commit(self): pass

    @abstractmethod
    def close(self): pass


class SQLiteService(IDatabaseService):
    def __init__(self, db_name="newusers.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.initialize_db()

    def initialize_db(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            is_logged_in INTEGER DEFAULT 0
        )
        ''')
        self.commit()

    def connect(self):
        pass  # already connected in __init__

    def execute(self, query, params=()):
        self.cursor.execute(query, params)

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()


# --------------------- User Entity ---------------------
class User:
    def __init__(self, username: str, password: str, is_logged_in: int = 0):
        self.username = username
        self.password = password  # hashed password
        self.is_logged_in = is_logged_in


# --------------------- User Service ---------------------
class UserService:
    def __init__(self, db_service: IDatabaseService):
        self.db = db_service

    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username: str, password: str) -> str:
        self.db.execute("SELECT * FROM users WHERE username = ?", (username,))
        if self.db.fetchone():
            return "Username already exists."

        hashed_password = self.hash_password(password)
        self.db.execute("INSERT INTO users (username, password, is_logged_in) VALUES (?, ?, 0)",
                        (username, hashed_password))
        self.db.commit()
        return "Registration successful."

    def login_user(self, username: str, password: str) -> str:
        self.db.execute("SELECT COUNT(*) FROM users WHERE is_logged_in = 1")
        if self.db.fetchone()[0] > 0:
            return "Another user is already logged in. Please logout first."

        self.db.execute("SELECT password FROM users WHERE username = ?", (username,))
        result = self.db.fetchone()
        if not result:
            return "Username does not exist."

        stored_password = result[0]
        if self.hash_password(password) == stored_password:
            self.db.execute("UPDATE users SET is_logged_in = 1 WHERE username = ?", (username,))
            self.db.commit()
            return "Login successful."
        else:
            return "Incorrect password."

    def logout_user(self, username: str) -> str:
        self.db.execute("SELECT is_logged_in FROM users WHERE username = ?", (username,))
        result = self.db.fetchone()
        if not result:
            return "Username does not exist."
        elif result[0] == 0:
            return "User is not logged in."
        else:
            self.db.execute("UPDATE users SET is_logged_in = 0 WHERE username = ?", (username,))
            self.db.commit()
            return "Logout successful."

    def change_password(self, username: str, old_password: str, new_password: str) -> str:
        self.db.execute("SELECT password, is_logged_in FROM users WHERE username = ?", (username,))
        result = self.db.fetchone()
        if not result:
            return "Username does not exist."
        stored_password, is_logged_in = result
        if is_logged_in == 0:
            return "You must be logged in to change your password."
        if self.hash_password(old_password) != stored_password:
            return "Incorrect current password."

        new_hashed = self.hash_password(new_password)
        self.db.execute("UPDATE users SET password = ? WHERE username = ?", (new_hashed, username))
        self.db.commit()
        return "Password changed successfully."


# --------------------- Application Interface ---------------------
class UserApp:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def run(self):
        while True:
            print("\n======= User Management System =======")
            print("1. Register")
            print("2. Login")
            print("3. Logout")
            print("4. Change Password")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                username = input("Enter username: ")
                password = getpass.getpass("Enter password (hidden): ")
                print(self.user_service.register_user(username, password))

            elif choice == "2":
                username = input("Enter username: ")
                password = getpass.getpass("Enter password (hidden): ")
                print(self.user_service.login_user(username, password))

            elif choice == "3":
                username = input("Enter username: ")
                print(self.user_service.logout_user(username))

            elif choice == "4":
                username = input("Enter username: ")
                old_password = getpass.getpass("Enter current password (hidden): ")
                new_password = getpass.getpass("Enter new password (hidden): ")
                print(self.user_service.change_password(username, old_password, new_password))

            elif choice == "5":
                print("Program Executed")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")


# --------------------- Main Execution ---------------------
if __name__ == "__main__":
    db = SQLiteService()
    user_service = UserService(db)
    app = UserApp(user_service)
    app.run()
    db.close()
