
import sqlite3


def view_all_job_seekers():

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, email, skills
        FROM job_seekers
        ORDER BY id DESC
    """)

    users = cursor.fetchall()
    connection.close()

    print("\n========== REGISTERED JOB SEEKERS ==========")

    if not users:
        print("\nNo job seekers registered.")
        return

    for user in users:
        print("\n-----------------------------------")
        print("User ID :", user[0])
        print("Name    :", user[1])
        print("Email   :", user[2])
        print("Skills  :", user[3])
        print("-----------------------------------")


def view_all_employers():

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, company_name, email, industry
        FROM employers
        ORDER BY id DESC
    """)

    employers = cursor.fetchall()
    connection.close()

    print("\n========== REGISTERED EMPLOYERS ==========")

    if not employers:
        print("\nNo employers registered.")
        return

    for employer in employers:
        print("\n-----------------------------------")
        print("Employer ID :", employer[0])
        print("Company     :", employer[1])
        print("Email       :", employer[2])
        print("Industry    :", employer[3])
        print("-----------------------------------")
