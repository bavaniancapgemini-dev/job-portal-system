
import sqlite3
from getpass import getpass

from admin.security import hash_password


def register_job_seeker():

    print("\n===================================")
    print("       JOB SEEKER REGISTRATION")
    print("===================================")

    name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip().lower()
    password = getpass("Create a password: ")
    confirm_password = getpass("Confirm your password: ")
    skills = input("Enter your skills: ").strip()

    if not name or not email or not password or not skills:
        print("\nAll fields are required.")
        return

    if password != confirm_password:
        print("\nPasswords do not match.")
        return

    if len(password) < 8:
        print("\nPassword must contain at least 8 characters.")
        return

    password_hash = hash_password(password)

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    try:

        cursor.execute("""
            INSERT INTO job_seekers (name, email, password, skills)
            VALUES (?, ?, ?, ?)
        """, (name, email, password_hash, skills))

        connection.commit()

        print("\nRegistration Successful!")
        print("-----------------------------------")
        print("Name:", name)
        print("Email:", email)
        print("Skills:", skills)
        print("-----------------------------------")

    except sqlite3.IntegrityError:
        print("\nThis email is already registered.")

    finally:
        connection.close()
