import sqlite3


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
        print("-----------------------------------")
        print("Welcome,", user[1])
        print("Email:", user[2])
        print("Skills:", user[3])
        print("-----------------------------------")

        return user

    else:
        print("\nInvalid email or password.")
        return None