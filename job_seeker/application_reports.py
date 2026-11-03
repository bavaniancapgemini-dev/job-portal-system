
import sqlite3
import csv
import os


def export_application_report(user):

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            applications.id,
            jobs.title,
            jobs.company_name,
            jobs.location,
            jobs.salary,
            jobs.job_type,
            applications.status
        FROM applications
        JOIN jobs ON applications.job_id = jobs.id
        WHERE applications.job_seeker_id = ?
        ORDER BY applications.id DESC
    """, (user[0],))

    applications = cursor.fetchall()
    connection.close()

    if not applications:
        print("\nNo applications available to export.")
        return

    filename = f"application_report_{user[0]}.csv"

    filepath = os.path.join(
        os.getcwd(),
        filename
    )

    with open(filepath, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Application ID",
            "Job Title",
            "Company",
            "Location",
            "Salary",
            "Job Type",
            "Application Status"
        ])

        writer.writerows(applications)

    print("\nApplication report exported successfully!")
    print("File location:", filepath)
