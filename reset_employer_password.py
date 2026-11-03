
import sqlite3
from getpass import getpass

connection = sqlite3.connect("job_portal.db")
cursor = connection.cursor()

email = input("Enter employer email: ").strip()

cursor.execute(
    "SELECT id, company_name FROM employers WHERE email = ?",
    (email,)
)

employer = cursor.fetchone()

if employer:
    print("\nCompany:", employer[1])

    new_password = getpass("Enter your new password: ")
    confirm_password = getpass("Confirm your new password: ")

    if new_password and new_password == confirm_password:

        cursor.execute("""
            UPDATE employers
            SET password = ?
            WHERE email = ?
        """, (new_password, email))

        connection.commit()
        print("\nPassword reset successfully!")

    else:
        print("\nPasswords do not match or are empty.")

else:
    print("\nEmployer account not found.")

connection.close()
