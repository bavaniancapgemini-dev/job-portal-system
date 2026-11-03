
import sqlite3


def save_job(user):

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    job_seeker_id = user[0]

    cursor.execute("""
        SELECT id, title, company_name, location
        FROM jobs
    """)

    jobs = cursor.fetchall()

    if not jobs:
        print("\nNo jobs available.")
        connection.close()
        return

    print("\n========== AVAILABLE JOBS ==========")

    for job in jobs:
        print("\nJob ID:", job[0])
        print("Title:", job[1])
        print("Company:", job[2])
        print("Location:", job[3])

    try:
        job_id = int(input("\nEnter Job ID to save: "))
    except ValueError:
        print("Invalid Job ID.")
        connection.close()
        return

    cursor.execute(
        "SELECT id FROM jobs WHERE id = ?", (job_id,)
    )

    if not cursor.fetchone():
        print("\nJob not found.")
    else:
        try:
            cursor.execute("""
                INSERT INTO saved_jobs (job_seeker_id, job_id)
                VALUES (?, ?)
            """, (job_seeker_id, job_id))

            connection.commit()
            print("\nJob saved successfully!")

        except sqlite3.IntegrityError:
            print("\nYou have already saved this job.")

    connection.close()


def view_saved_jobs(user):

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT saved_jobs.job_id, jobs.title,
               jobs.company_name, jobs.location, jobs.salary
        FROM saved_jobs
        JOIN jobs ON saved_jobs.job_id = jobs.id
        WHERE saved_jobs.job_seeker_id = ?
    """, (user[0],))

    jobs = cursor.fetchall()

    if jobs:
        print("\n========== YOUR SAVED JOBS ==========")

        for job in jobs:
            print("\nJob ID:", job[0])
            print("Title:", job[1])
            print("Company:", job[2])
            print("Location:", job[3])
            print("Salary:", job[4])

    else:
        print("\nNo saved jobs found.")

    connection.close()


def remove_saved_job(user):

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT saved_jobs.job_id, jobs.title, jobs.company_name
        FROM saved_jobs
        JOIN jobs ON saved_jobs.job_id = jobs.id
        WHERE saved_jobs.job_seeker_id = ?
    """, (user[0],))

    jobs = cursor.fetchall()

    if not jobs:
        print("\nNo saved jobs to remove.")
        connection.close()
        return

    print("\n========== SAVED JOBS ==========")

    for job in jobs:
        print("\nJob ID:", job[0])
        print("Title:", job[1])
        print("Company:", job[2])

    try:
        job_id = int(input("\nEnter Job ID to remove: "))
    except ValueError:
        print("Invalid Job ID.")
        connection.close()
        return

    cursor.execute("""
        DELETE FROM saved_jobs
        WHERE job_id = ? AND job_seeker_id = ?
    """, (job_id, user[0]))

    if cursor.rowcount > 0:
        connection.commit()
        print("\nSaved job removed successfully!")
    else:
        print("\nThis job is not in your saved jobs.")

    connection.close()
