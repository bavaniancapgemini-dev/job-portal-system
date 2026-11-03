
import sqlite3
import csv
import os


def export_employer_report(employer):

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    employer_id = employer[0]

    cursor.execute("""
        SELECT
            jobs.title,
            job_seekers.name,
            job_seekers.email,
            job_seekers.skills,
            applications.status
        FROM applications
        JOIN jobs
            ON applications.job_id = jobs.id
        JOIN job_seekers
            ON applications.job_seeker_id = job_seekers.id
        WHERE jobs.employer_id = ?
        ORDER BY applications.id DESC
    """, (employer_id,))

    applicants = cursor.fetchall()
    connection.close()

    if not applicants:
        print("\nNo applicants available to export.")
        return

    filename = f"employer_report_{employer_id}.csv"

    filepath = os.path.join(os.getcwd(), filename)

    with open(filepath, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Job Title",
            "Applicant Name",
            "Email",
            "Skills",
            "Application Status"
        ])

        writer.writerows(applicants)

    print("\nEmployer report exported successfully!")
    print("File location:", filepath)
