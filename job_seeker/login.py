import sqlite3
from job_seeker.dashboard import job_seeker_dashboard


def login_job_seeker():
    print("\n===================================")
    print("          JOB SEEKER LOGIN")
    print("===================================")

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, email, skills
        FROM job_seekers
        WHERE email = ? AND password = ?
    """, (email, password))

    user = cursor.fetchone()

    connection.close()

    if user:
        print("\nLogin Successful!")
        print("Welcome,", user[1])

        job_seeker_dashboard(user)

        return user

    else:
        print("\nInvalid email or password.")
        return None