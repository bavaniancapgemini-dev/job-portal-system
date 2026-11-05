
import sqlite3


def view_platform_statistics():

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    # Total Job Seekers
    cursor.execute("SELECT COUNT(*) FROM job_seekers")
    total_seekers = cursor.fetchone()[0]

    # Total Employers
    cursor.execute("SELECT COUNT(*) FROM employers")
    total_employers = cursor.fetchone()[0]

    # Total Jobs
    cursor.execute("SELECT COUNT(*) FROM jobs")
    total_jobs = cursor.fetchone()[0]

    # Open Jobs
    cursor.execute("SELECT COUNT(*) FROM jobs WHERE is_open = 1")
    open_jobs = cursor.fetchone()[0]

    # Closed Jobs
    cursor.execute("SELECT COUNT(*) FROM jobs WHERE is_open = 0")
    closed_jobs = cursor.fetchone()[0]

    # Total Applications
    cursor.execute("SELECT COUNT(*) FROM applications")
    total_applications = cursor.fetchone()[0]

    # Total Admins
    cursor.execute("SELECT COUNT(*) FROM admins")
    total_admins = cursor.fetchone()[0]

    connection.close()

    print("\n===================================")
    print("       PLATFORM STATISTICS")
    print("===================================")

    print("\nUSER STATISTICS")
    print("-----------------------------------")
    print("Total Job Seekers :", total_seekers)
    print("Total Employers   :", total_employers)
    print("Total Admins      :", total_admins)

    print("\nJOB STATISTICS")
    print("-----------------------------------")
    print("Total Jobs        :", total_jobs)
    print("Open Jobs         :", open_jobs)
    print("Closed Jobs       :", closed_jobs)

    print("\nAPPLICATION STATISTICS")
    print("-----------------------------------")
    print("Total Applications:", total_applications)

    print("\n===================================")
