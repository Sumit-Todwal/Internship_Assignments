from flask import Blueprint, render_template, request, redirect, session, url_for
from app.models.database import get_connection
import sqlite3

device_bp = Blueprint("device",__name__)

# @device_bp.route("/device-form",methods = ["GET","POST"])
# def device_form():
#     if request.method == "POST":
#         return redirect("dashboard.dashboard")
#     return render_template("device_form.html")

@device_bp.route("/device-form", methods=["GET", "POST"])
def device_form():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        device_name = request.form.get("device_name")
        location = request.form.get("location")

        if device_name:  # simple validation
            conn = sqlite3.connect("instance/database.db")
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO devices (user_id, device_name, location)
                VALUES (?, ?, ?)
            ''', (session["user_id"], device_name, location))
            conn.commit()
            conn.close()

        return redirect(url_for("dashboard.dashboard"))

    return render_template("device_form.html")