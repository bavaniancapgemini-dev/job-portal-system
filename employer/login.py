
import sqlite3
from getpass import getpass

from admin.security import (
    hash_password,
    verify_password
)

from employer.dashboard import employer_dashboard


def login_employer():

    print("\n===================================")
    print("          EMPLOYER LOGIN")
    print("===================================")

    email = input("Enter your email: ").strip().lower()
    password = getpass("Enter your password: ")

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    try:

        cursor.execute("""
            SELECT id, company_name, email, password, industry
            FROM employers
            WHERE email = ?
        """, (email,))

        employer = cursor.fetchone()

        if not employer:
            print("\nInvalid email or password.")
            return None

        stored_password = employer[3]

        if stored_password.startswith("pbkdf2_sha256$"):

            password_valid = verify_password(
                password,
                stored_password
            )

        else:
            # Support existing accounts with plain-text passwords.
            password_valid = password == stored_password

            if password_valid:

                new_password_hash = hash_password(password)

                cursor.execute("""
                    UPDATE employers
                    SET password = ?
                    WHERE id = ?
                """, (new_password_hash, employer[0]))

                connection.commit()

        if password_valid:

            print("\nLogin Successful!")
            print("Welcome,", employer[1])

            # Preserve the original dashboard data structure:
            # (id, company_name, email, industry)
            dashboard_employer = (
                employer[0],
                employer[1],
                employer[2],
                employer[4]
            )

        else:
            print("\nInvalid email or password.")
            return None

    finally:
        connection.close()

    employer_dashboard(dashboard_employer)

    return dashboard_employer
