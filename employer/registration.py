
import sqlite3
from getpass import getpass

from admin.security import hash_password


def register_employer():

    print("\n===================================")
    print("        EMPLOYER REGISTRATION")
    print("===================================")

    company_name = input("Enter company name: ").strip()
    email = input("Enter company email: ").strip().lower()
    password = getpass("Create a password: ")
    confirm_password = getpass("Confirm your password: ")
    industry = input("Enter industry: ").strip()

    if not company_name or not email or not password or not industry:
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
            INSERT INTO employers
            (company_name, email, password, industry)
            VALUES (?, ?, ?, ?)
        """, (company_name, email, password_hash, industry))

        connection.commit()

        print("\nEmployer Registration Successful!")
        print("-----------------------------------")
        print("Company :", company_name)
        print("Email   :", email)
        print("Industry:", industry)
        print("-----------------------------------")

    except sqlite3.IntegrityError:
        print("\nThis company email is already registered.")

    finally:
        connection.close()
