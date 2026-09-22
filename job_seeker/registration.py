import sqlite3


def register_job_seeker():
    print("\n===================================")
    print("       JOB SEEKER REGISTRATION")
    print("===================================")

    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Create a password: ")
    skills = input("Enter your skills: ")

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO job_seekers (name, email, password, skills)
            VALUES (?, ?, ?, ?)
        """, (name, email, password, skills))

        connection.commit()

        print("\nRegistration Successful!")
        print("-----------------------------------")
        print("Name:", name)
        print("Email:", email)
        print("Skills:", skills)
        print("-----------------------------------")

    except sqlite3.IntegrityError:
        print("\nThis email is already registered.")

    connection.close()