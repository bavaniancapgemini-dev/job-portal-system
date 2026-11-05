
import sqlite3
import csv
import os
from datetime import datetime
from admin.activity_logs import log_admin_activity


def export_job_seekers(admin_name):
    
    log_admin_activity(
        admin_name,
        "Report Exported",
        "Exported Job Seeker Report"
    )

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, email, skills
        FROM job_seekers
    """)

    records = cursor.fetchall()
    connection.close()

    os.makedirs("admin_reports", exist_ok=True)

    filename = os.path.join(
        "admin_reports",
        "job_seekers_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".csv"
    )

    with open(filename, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(["ID", "Name", "Email", "Skills"])
        writer.writerows(records)

    print("\nJob Seeker Report Exported!")
    print("File:", filename)


def export_employers(admin_name):

    log_admin_activity(
        admin_name,
        "Report Exported",
        "Exported Employer Report"
    )

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, company_name, email, industry
        FROM employers
    """)

    records = cursor.fetchall()
    connection.close()

    os.makedirs("admin_reports", exist_ok=True)

    filename = os.path.join(
        "admin_reports",
        "employers_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".csv"
    )

    with open(filename, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(["ID", "Company Name", "Email", "Industry"])
        writer.writerows(records)

    print("\nEmployer Report Exported!")
    print("File:", filename)


def export_jobs(admin_name):
    
    log_admin_activity(
        admin_name,
        "Report Exported",
        "Exported Job Report"
    )

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, title, company_name, location,
               salary, job_type, is_open
        FROM jobs
    """)

    records = cursor.fetchall()
    connection.close()

    os.makedirs("admin_reports", exist_ok=True)

    filename = os.path.join(
        "admin_reports",
        "jobs_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".csv"
    )

    with open(filename, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "ID", "Job Title", "Company", "Location",
            "Salary", "Job Type", "Status"
        ])

        for job in records:
            writer.writerow([
                job[0], job[1], job[2], job[3],
                job[4], job[5],
                "Open" if job[6] else "Closed"
            ])

    print("\nJob Report Exported!")
    print("File:", filename)


def export_applications(admin_name):

    log_admin_activity(
        admin_name,
        "Report Exported",
        "Exported Application Report"
    )

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
    """)

    records = cursor.fetchall()
    connection.close()

    os.makedirs("admin_reports", exist_ok=True)

    filename = os.path.join(
        "admin_reports",
        "applications_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".csv"
    )

    with open(filename, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Application ID",
            "Applicant",
            "Job Title",
            "Company",
            "Status"
        ])

        writer.writerows(records)

    print("\nApplication Report Exported!")
    print("File:", filename)
