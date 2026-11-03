
import sqlite3


def admin_login():

    print("\n===================================")
    print("           ADMIN LOGIN")
    print("===================================")

    email = input("Enter Admin Email: ").strip()
    password = input("Enter Admin Password: ")

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, email, password
        FROM admins
        WHERE email = ? AND password = ?
    """, (email, password))

    admin = cursor.fetchone()

    connection.close()

    if admin:
        print("\nAdmin Login Successful!")
        print("Welcome,", admin[1])
        return admin

    else:
        print("\nInvalid Admin Email or Password.")
        return None
