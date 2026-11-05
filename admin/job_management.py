
import sqlite3


def view_all_jobs():

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            jobs.id,
            jobs.title,
            jobs.company_name,
            jobs.location,
            jobs.salary,
            jobs.job_type,
            jobs.is_open
        FROM jobs
        ORDER BY jobs.id DESC
    """)

    jobs = cursor.fetchall()
    connection.close()

    print("\n========== ALL JOB POSTINGS ==========")

    if not jobs:
        print("\nNo jobs available.")
        return

    for job in jobs:
        print("\n-----------------------------------")
        print("Job ID     :", job[0])
        print("Title      :", job[1])
        print("Company    :", job[2])
        print("Location   :", job[3])
        print("Salary     :", job[4])
        print("Job Type   :", job[5])
        print("Status     :", "Open" if job[6] else "Closed")
        print("-----------------------------------")


def delete_job_as_admin():

    print("\n========== DELETE JOB POSTING ==========")

    try:
        job_id = int(input("Enter Job ID to delete: "))
    except ValueError:
        print("\nPlease enter a valid Job ID.")
        return

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, title, company_name
        FROM jobs
        WHERE id = ?
    """, (job_id,))

    job = cursor.fetchone()

    if not job:
        print("\nJob not found.")
        connection.close()
        return

    print("\nJob Details")
    print("-----------------------------------")
    print("Job ID  :", job[0])
    print("Title   :", job[1])
    print("Company :", job[2])
    print("-----------------------------------")

    confirm = input(
        "Are you sure you want to delete this job? (yes/no): "
    ).strip().lower()

    if confirm == "yes":

        cursor.execute("""
            DELETE FROM applications
            WHERE job_id = ?
        """, (job_id,))

        cursor.execute("""
            DELETE FROM saved_jobs
            WHERE job_id = ?
        """, (job_id,))

        cursor.execute("""
            DELETE FROM jobs
            WHERE id = ?
        """, (job_id,))

        connection.commit()

        print("\nJob posting deleted successfully!")

    else:
        print("\nDeletion cancelled.")

    connection.close()
