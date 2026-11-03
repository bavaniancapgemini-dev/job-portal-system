
import sqlite3


def view_notifications(user):

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            jobs.title,
            jobs.company_name,
            applications.status
        FROM applications
        JOIN jobs
            ON applications.job_id = jobs.id
        WHERE applications.job_seeker_id = ?
        ORDER BY applications.id DESC
    """, (user[0],))

    notifications = cursor.fetchall()
    connection.close()

    print("\n========== MY NOTIFICATIONS ==========")

    if not notifications:
        print("\nYou have no notifications yet.")
        return

    for title, company, status in notifications:

        print("\nJob:", title)
        print("Company:", company)

        if status == "Shortlisted":
            print("Notification: Congratulations! You have been shortlisted.")

        elif status == "Rejected":
            print("Notification: Unfortunately, your application was rejected.")

        elif status == "Selected":
            print("Notification: Congratulations! You have been selected!")

        else:
            print("Notification: Your application is under review.")

        print("--------------------------------------")
