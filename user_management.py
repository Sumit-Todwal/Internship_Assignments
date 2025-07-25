import sqlite3
import hashlib
import getpass

# Create database and users table if it doesn't exist
conn = sqlite3.connect("newusers.db")
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    is_logged_in INTEGER DEFAULT 0
)
''')
conn.commit()

# Main program
while True:
    print("\n======= User Management System =======")
    print("1. Register")
    print("2. Login")
    print("3. Logout")
    print("4. Change Password")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    # Register
    if choice == "1":
        print("\n--- Register ---")
        username = input("Enter username: ")

        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            print("Username already exists. Please try another.")
        else:
            password = getpass.getpass("Enter password (hidden): ")
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            cursor.execute("INSERT INTO users (username, password, is_logged_in) VALUES (?, ?, 0)", (username, hashed_password))
            conn.commit()
            print("Registration successful.")

    # Login
    elif choice == "2":
        print("\n--- Login ---")

        # Check if any user is already logged in
        cursor.execute("SELECT COUNT(*) FROM users WHERE is_logged_in = 1")
        if cursor.fetchone()[0] > 0:
            print("A user is already logged in. Please logout first.")
            continue

        username = input("Enter username: ")
        password = getpass.getpass("Enter password (hidden): ")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        if result is None:
            print("Username does not exist.")
        else:
            stored_password = result[0]
            if hashed_password == stored_password:
                cursor.execute("UPDATE users SET is_logged_in = 1 WHERE username = ?", (username,))
                conn.commit()
                print("Login successful.")
            else:
                print("Incorrect password.")

    # Logout
    elif choice == "3":
        print("\n--- Logout ---")
        username = input("Enter username: ")
        cursor.execute("SELECT is_logged_in FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        if result is None:
            print("Username does not exist.")
        elif result[0] == 0:
            print("User is not logged in.")
        else:
            cursor.execute("UPDATE users SET is_logged_in = 0 WHERE username = ?", (username,))
            conn.commit()
            print("Logout successful.")

    # Change Password
    elif choice == "4":
        print("\n--- Change Password ---")
        username = input("Enter username: ")
        cursor.execute("SELECT password, is_logged_in FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        if result is None:
            print("Username does not exist.")
        else:
            stored_password = result[0]
            logged_in = result[1]
            if logged_in == 0:
                print("You must be logged in to change your password.")
            else:
                old_password = getpass.getpass("Enter current password (hidden): ")
                hashed_old_password = hashlib.sha256(old_password.encode()).hexdigest()
                if hashed_old_password != stored_password:
                    print("Incorrect current password.")
                else:
                    new_password = getpass.getpass("Enter new password (hidden): ")
                    hashed_new_password = hashlib.sha256(new_password.encode()).hexdigest()
                    cursor.execute("UPDATE users SET password = ? WHERE username = ?", (hashed_new_password, username))
                    conn.commit()
                    print("Password changed successfully.")

    # Exit
    elif choice == "5":
        print("Program Executed")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")

# Close connection
conn.close()