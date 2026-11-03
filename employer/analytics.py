
import sqlite3


def employer_analytics(employer):

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    employer_id = employer[0]

    # Total jobs posted
    cursor.execute("""
        SELECT COUNT(*)
        FROM jobs
        WHERE employer_id = ?
    """, (employer_id,))

    total_jobs = cursor.fetchone()[0]

    # Total applications
    cursor.execute("""
        SELECT COUNT(*)
        FROM applications
        JOIN jobs ON applications.job_id = jobs.id
        WHERE jobs.employer_id = ?
    """, (employer_id,))

    total_applications = cursor.fetchone()[0]

    # Application statuses
    cursor.execute("""
        SELECT applications.status, COUNT(*)
        FROM applications
        JOIN jobs ON applications.job_id = jobs.id
        WHERE jobs.employer_id = ?
        GROUP BY applications.status
    """, (employer_id,))

    statuses = cursor.fetchall()

    status_counts = {
        "Applied": 0,
        "Shortlisted": 0,
        "Selected": 0,
        "Rejected": 0
    }

    for status, count in statuses:
        status_counts[status] = count

    # Applications per job
    cursor.execute("""
        SELECT jobs.title, COUNT(applications.id)
        FROM jobs
        LEFT JOIN applications
            ON jobs.id = applications.job_id
        WHERE jobs.employer_id = ?
        GROUP BY jobs.id, jobs.title
    """, (employer_id,))

    job_reports = cursor.fetchall()

    connection.close()

    print("\n========== EMPLOYER ANALYTICS ==========")

    print("\nTotal Jobs Posted:", total_jobs)
    print("Total Applications:", total_applications)

    print("\n========== APPLICATION STATUS ==========")

    print("Applied:", status_counts["Applied"])
    print("Shortlisted:", status_counts["Shortlisted"])
    print("Selected:", status_counts["Selected"])
    print("Rejected:", status_counts["Rejected"])

    print("\n========== JOB-WISE REPORT ==========")

    if job_reports:
        for title, count in job_reports:
            print(f"{title}: {count} applications")
    else:
        print("No jobs posted yet.")

    print("\n========================================")
