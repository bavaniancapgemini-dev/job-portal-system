
import sqlite3
from admin.activity_logs import log_admin_activity


def view_all_job_seekers():

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, email, skills
        FROM job_seekers
        ORDER BY id DESC
    """)

    users = cursor.fetchall()
    connection.close()

    print("\n========== REGISTERED JOB SEEKERS ==========")

    if not users:
        print("\nNo job seekers registered.")
        return

    for user in users:
        print("\n-----------------------------------")
        print("User ID :", user[0])
        print("Name    :", user[1])
        print("Email   :", user[2])
        print("Skills  :", user[3])
        print("-----------------------------------")


def view_all_employers():

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, company_name, email, industry
        FROM employers
        ORDER BY id DESC
    """)

    employers = cursor.fetchall()
    connection.close()

    print("\n========== REGISTERED EMPLOYERS ==========")

    if not employers:
        print("\nNo employers registered.")
        return

    for employer in employers:
        print("\n-----------------------------------")
        print("Employer ID :", employer[0])
        print("Company     :", employer[1])
        print("Email       :", employer[2])
        print("Industry    :", employer[3])
        print("-----------------------------------")
        

def search_users():

    search_term = input(
        "\nEnter user name or email to search: "
    ).strip()

    if not search_term:
        print("\nPlease enter a search term.")
        return

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    pattern = "%" + search_term + "%"

    cursor.execute("""
        SELECT id, name, email, skills
        FROM job_seekers
        WHERE name LIKE ? OR email LIKE ?
    """, (pattern, pattern))

    seekers = cursor.fetchall()

    cursor.execute("""
        SELECT id, company_name, email, industry
        FROM employers
        WHERE company_name LIKE ? OR email LIKE ?
    """, (pattern, pattern))

    employers = cursor.fetchall()

    connection.close()

    print("\n========== SEARCH RESULTS ==========")

    if not seekers and not employers:
        print("\nNo matching users found.")
        return

    print("\nJOB SEEKERS")

    for user in seekers:
        print("-----------------------------------")
        print("ID     :", user[0])
        print("Name   :", user[1])
        print("Email  :", user[2])
        print("Skills :", user[3])

    print("\nEMPLOYERS")

    for employer in employers:
        print("-----------------------------------")
        print("ID       :", employer[0])
        print("Company  :", employer[1])
        print("Email    :", employer[2])
        print("Industry :", employer[3])

    print("-----------------------------------")


def delete_user_account(admin_name):

    print("\n========== DELETE USER ACCOUNT ==========")
    print("1. Delete Job Seeker")
    print("2. Delete Employer")

    choice = input("\nSelect account type: ").strip()

    if choice not in ["1", "2"]:
        print("\nInvalid choice.")
        return

    try:
        user_id = int(input("Enter User/Employer ID: "))
    except ValueError:
        print("\nPlease enter a valid ID.")
        return

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    try:

        if choice == "1":

            cursor.execute("""
                SELECT id, name, email
                FROM job_seekers
                WHERE id = ?
            """, (user_id,))

            user = cursor.fetchone()

            if not user:
                print("\nJob seeker not found.")
                return

            print("\nAccount:", user[1], "|", user[2])

            confirm = input(
                "Permanently delete this account? (yes/no): "
            ).strip().lower()

            if confirm != "yes":
                print("\nDeletion cancelled.")
                return

            cursor.execute(
                "DELETE FROM applications WHERE job_seeker_id = ?",
                (user_id,)
            )

            cursor.execute(
                "DELETE FROM saved_jobs WHERE job_seeker_id = ?",
                (user_id,)
            )

            cursor.execute(
                "DELETE FROM job_seekers WHERE id = ?",
                (user_id,)
            )

        else:

            cursor.execute("""
                SELECT id, company_name, email
                FROM employers
                WHERE id = ?
            """, (user_id,))

            employer = cursor.fetchone()

            if not employer:
                print("\nEmployer not found.")
                return

            print("\nCompany:", employer[1], "|", employer[2])

            confirm = input(
                "Permanently delete this account? (yes/no): "
            ).strip().lower()

            if confirm != "yes":
                print("\nDeletion cancelled.")
                return

            cursor.execute("""
                SELECT id FROM jobs WHERE employer_id = ?
            """, (user_id,))

            job_ids = cursor.fetchall()

            for job in job_ids:

                cursor.execute(
                    "DELETE FROM applications WHERE job_id = ?",
                    (job[0],)
                )

                cursor.execute(
                    "DELETE FROM saved_jobs WHERE job_id = ?",
                    (job[0],)
                )

            cursor.execute(
                "DELETE FROM jobs WHERE employer_id = ?",
                (user_id,)
            )

            cursor.execute(
                "DELETE FROM employers WHERE id = ?",
                (user_id,)
            )

        connection.commit()
        
        if choice == "1":
            action = "Job Seeker Account Deleted"
            details = f"Deleted Job Seeker ID: {user_id}"

        else:
            action = "Employer Account Deleted"
            details = f"Deleted Employer ID: {user_id}"

        log_admin_activity(
            admin_name,
            action,
            details
        )
        
        print("\nAccount deleted successfully!")

    except sqlite3.Error as error:
        connection.rollback()
        print("\nDatabase error:", error)

    finally:
        connection.close()

