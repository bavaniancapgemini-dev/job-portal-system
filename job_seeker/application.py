
import sqlite3


def apply_for_job(user):
    print("\n===================================")
    print("           APPLY FOR JOB")
    print("===================================")

    job_id = input("Enter Job ID: ")

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    # Check whether the job exists and is open
    cursor.execute("""
        SELECT id, title, company_name, location
        FROM jobs
        WHERE id = ? AND is_open = 1
    """, (job_id,))

    job = cursor.fetchone()

    if not job:
        print("\nJob not found or this vacancy is closed.")
        connection.close()
        return

    print("\nJob Details")
    print("-----------------------------------")
    print("Job ID   :", job[0])
    print("Title    :", job[1])
    print("Company  :", job[2])
    print("Location :", job[3])
    print("-----------------------------------")

    confirm = input("Do you want to apply for this job? (yes/no): ")

    if confirm.lower() != "yes":
        print("\nApplication cancelled.")
        connection.close()
        return

    # Check for duplicate applications
    cursor.execute("""
        SELECT id
        FROM applications
        WHERE job_id = ? AND job_seeker_id = ?
    """, (job_id, user[0]))

    existing_application = cursor.fetchone()

    if existing_application:
        print("\nYou have already applied for this job.")
        connection.close()
        return

    # Submit application
    cursor.execute("""
        INSERT INTO applications
        (job_id, job_seeker_id, status)
        VALUES (?, ?, ?)
    """, (job_id, user[0], "Applied"))

    connection.commit()
    connection.close()

    print("\nApplication submitted successfully!")
    print("-----------------------------------")
    print("Job       :", job[1])
    print("Company   :", job[2])
    print("Status    : Applied")
    print("-----------------------------------")
