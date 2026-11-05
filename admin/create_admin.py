
import sqlite3
from getpass import getpass

from admin.security import hash_password


def create_admin():

    print("\n===================================")
    print("       CREATE ADMIN ACCOUNT")
    print("===================================")

    name = input("Enter Admin Name: ").strip()
    email = input("Enter Admin Email: ").strip().lower()

    password = getpass("Create Admin Password: ")
    confirm_password = getpass("Confirm Admin Password: ")

    if not name or not email or not password:
        print("\nAll fields are required.")
        return

    if password != confirm_password:
        print("\nPasswords do not match.")
        return

    password_hash = hash_password(password)

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    try:

        cursor.execute("""
            INSERT INTO admins (name, email, password)
            VALUES (?, ?, ?)
        """, (name, email, password_hash))

        connection.commit()

        print("\nAdmin account created successfully!")
        print("Admin Name:", name)
        print("Admin Email:", email)

    except sqlite3.IntegrityError:
        print("\nAn admin account with this email already exists.")

    finally:
        connection.close()


if __name__ == "__main__":
    create_admin()
