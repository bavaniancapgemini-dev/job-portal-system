
import sqlite3
from datetime import datetime


def create_activity_table():

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS admin_activity_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            admin_name TEXT NOT NULL,
            action TEXT NOT NULL,
            details TEXT,
            activity_time TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def log_admin_activity(admin_name, action, details=""):

    create_activity_table()

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    activity_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    cursor.execute("""
        INSERT INTO admin_activity_logs (
            admin_name,
            action,
            details,
            activity_time
        )
        VALUES (?, ?, ?, ?)
    """, (
        admin_name,
        action,
        details,
        activity_time
    ))

    connection.commit()
    connection.close()


def view_admin_activity_logs():

    create_activity_table()

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT admin_name, action, details, activity_time
        FROM admin_activity_logs
        ORDER BY id DESC
    """)

    logs = cursor.fetchall()
    connection.close()

    print("\n========== ADMIN ACTIVITY LOGS ==========")

    if not logs:
        print("\nNo activity recorded yet.")
        return

    for log in logs:

        print("\n-----------------------------------")
        print("Admin  :", log[0])
        print("Action :", log[1])
        print("Details:", log[2])
        print("Time   :", log[3])
        print("-----------------------------------")
