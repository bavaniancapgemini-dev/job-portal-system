
import sqlite3


def view_all_applications():

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            applications.id,
            job_seekers.name,
            jobs.title,
            jobs.company_name,
            applications.status
        FROM applications
        JOIN job_seekers
            ON applications.job_seeker_id = job_seekers.id
        JOIN jobs
            ON applications.job_id = jobs.id
        ORDER BY applications.id DESC
    """)

    applications = cursor.fetchall()
    connection.close()

    print("\n========== ALL JOB APPLICATIONS ==========")

    if not applications:
        print("\nNo applications found.")
        return

    for application in applications:

        print("\n-----------------------------------")
        print("Application ID :", application[0])
        print("Applicant      :", application[1])
        print("Job Title      :", application[2])
        print("Company        :", application[3])
        print("Status         :", application[4])
        print("-----------------------------------")


def application_statistics():

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT status, COUNT(*)
        FROM applications
        GROUP BY status
    """)

    statistics = cursor.fetchall()

    cursor.execute("""
        SELECT COUNT(*) FROM applications
    """)

    total = cursor.fetchone()[0]

    connection.close()

    print("\n========== APPLICATION STATISTICS ==========")
    print("Total Applications:", total)

    if not statistics:
        print("\nNo application statistics available.")
        return

    for status, count in statistics:
        print(f"{status}: {count}")

    print("-----------------------------------")
