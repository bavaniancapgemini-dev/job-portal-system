
import sqlite3
from getpass import getpass

from admin.security import (
    hash_password,
    verify_password
)

from job_seeker.dashboard import job_seeker_dashboard


def login_job_seeker():

    print("\n===================================")
    print("          JOB SEEKER LOGIN")
    print("===================================")

    email = input("Enter your email: ").strip().lower()
    password = getpass("Enter your password: ")

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    try:

        cursor.execute("""
            SELECT id, name, email, password, skills
            FROM job_seekers
            WHERE email = ?
        """, (email,))

        user = cursor.fetchone()

        if not user:
            print("\nInvalid email or password.")
            return None

        stored_password = user[3]

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
                    UPDATE job_seekers
                    SET password = ?
                    WHERE id = ?
                """, (new_password_hash, user[0]))

                connection.commit()

        if password_valid:

            print("\nLogin Successful!")
            print("Welcome,", user[1])

            # Keep the original dashboard data structure:
            # (id, name, email, skills)
            dashboard_user = (
                user[0],
                user[1],
                user[2],
                user[4]
            )

        else:
            print("\nInvalid email or password.")
            return None

    finally:
        connection.close()

    job_seeker_dashboard(dashboard_user)

    return dashboard_user
