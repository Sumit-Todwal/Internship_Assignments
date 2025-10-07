from flask import Blueprint, session, render_template, redirect, url_for
import random
import sqlite3
from datetime import datetime

dashboard_bp = Blueprint("dashboard", __name__)

# def get_device_id_for_user(user_id):
#     conn = sqlite3.connect("instance/database.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT id FROM devices WHERE user_id = ?", (user_id,))
#     device = cursor.fetchone()
#     conn.close()
#     return device[0] if device else None

def get_devices_for_user(user_id):
    conn = sqlite3.connect("instance/database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, device_name, location FROM devices WHERE user_id = ?", (user_id,))
    devices = cursor.fetchall()
    conn.close()
    return devices


def homepage():
    return render_template(("dashboard.html"))




# @dashboard_bp.route("/dashboard")
# def dashboard():
#     if "user_id" not in session:
#         return redirect(url_for("auth.login"))

#     voltage = round(random.uniform(200, 250), 2)
#     current = round(random.uniform(0, 20), 2)
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     device_id = get_device_id_for_user(session["user_id"])
#     if device_id is not None:
#         conn = sqlite3.connect("instance/database.db")
#         cursor = conn.cursor()
#         cursor.execute('''
#             INSERT INTO energy_data (device_id, timestamp, current, voltage)
#             VALUES (?, ?, ?, ?)
#         ''', (device_id, timestamp, current, voltage))
#         conn.commit()
#         conn.close()

#     return render_template("dashboard.html", voltage=voltage, current=current)



@dashboard_bp.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    devices = get_devices_for_user(session["user_id"])
    
    # If no devices, redirect to device form
    if not devices:
        return redirect(url_for("device.device_form"))

    # Generate random energy data for each device
    energy_data = []
    conn = sqlite3.connect("instance/database.db")
    cursor = conn.cursor()
    
    for device in devices:
        device_id, device_name, device_type = device
        voltage = round(random.uniform(200, 250), 2)
        current = round(random.uniform(0, 20), 2)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute('''
            INSERT INTO energy_data (device_id, timestamp, current, voltage)
            VALUES (?, ?, ?, ?)
        ''', (device_id, timestamp, current, voltage))
        
        energy_data.append({
            "device_name": device_name,
            "device_type": device_type,
            "voltage": voltage,
            "current": current,
            "timestamp": timestamp
        })

    conn.commit()
    conn.close()

    return render_template("dashboard.html", devices=energy_data)