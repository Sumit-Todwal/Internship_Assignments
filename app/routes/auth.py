from flask import Blueprint, render_template, request, redirect, session, url_for
import sqlite3
import os

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("instance/database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
                        (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session["user_id"] = user[0]
            return redirect(url_for("device.device_form"))
        return "Invalid credentials"

    return render_template("login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("instance/database.db")
        cursor = conn.cursor()
        # print(os.path.abspath("instance/database.db"))

        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)"
                           , (username, password))
            conn.commit()
        except sqlite3.IntegrityError:
            return "Username already exists!"
        conn.close()
        return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))