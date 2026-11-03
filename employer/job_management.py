
import sqlite3


def manage_employer_jobs(employer):

    employer_id = employer[0]

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    # Add vacancy status column if it does not already exist
    cursor.execute("PRAGMA table_info(jobs)")
    columns = [column[1] for column in cursor.fetchall()]

    if "is_open" not in columns:
        cursor.execute("""
            ALTER TABLE jobs
            ADD COLUMN is_open INTEGER NOT NULL DEFAULT 1
        """)
        connection.commit()

    connection.close()

    while True:

        print("\n========== JOB MANAGEMENT ==========")
        print("1. View My Jobs")
        print("2. Edit Job Details")
        print("3. Close Job Vacancy")
        print("4. Reopen Job Vacancy")
        print("5. Delete Job")
        print("6. Back to Dashboard")

        choice = input("\nEnter your choice: ")

        connection = sqlite3.connect("job_portal.db")
        cursor = connection.cursor()

        if choice == "1":

            cursor.execute("""
                SELECT id, title, location, salary, job_type, is_open
                FROM jobs
                WHERE employer_id = ?
            """, (employer_id,))

            jobs = cursor.fetchall()

            if jobs:
                for job in jobs:
                    print("\nJob ID:", job[0])
                    print("Title:", job[1])
                    print("Location:", job[2])
                    print("Salary:", job[3])
                    print("Job Type:", job[4])
                    print("Status:", "Open" if job[5] else "Closed")
            else:
                print("\nYou have not posted any jobs.")

        elif choice == "2":

            job_id = input("Enter Job ID to edit: ")

            cursor.execute("""
                SELECT id FROM jobs
                WHERE id = ? AND employer_id = ?
            """, (job_id, employer_id))

            if cursor.fetchone():

                title = input("Enter new job title: ")
                location = input("Enter new location: ")
                salary = input("Enter new salary: ")
                job_type = input("Enter new job type: ")
                description = input("Enter new description: ")
                skills = input("Enter required skills: ")

                cursor.execute("""
                    UPDATE jobs
                    SET title = ?,
                        location = ?,
                        salary = ?,
                        job_type = ?,
                        description = ?,
                        skills = ?
                    WHERE id = ? AND employer_id = ?
                """, (
                    title, location, salary, job_type,
                    description, skills, job_id, employer_id
                ))

                connection.commit()
                print("\nJob details updated successfully!")

            else:
                print("\nJob not found.")

        elif choice == "3":

            job_id = input("Enter Job ID to close: ")

            cursor.execute("""
                UPDATE jobs
                SET is_open = 0
                WHERE id = ? AND employer_id = ?
            """, (job_id, employer_id))

            if cursor.rowcount:
                connection.commit()
                print("\nJob vacancy closed successfully!")
            else:
                print("\nJob not found.")

        elif choice == "4":

            job_id = input("Enter Job ID to reopen: ")

            cursor.execute("""
                UPDATE jobs
                SET is_open = 1
                WHERE id = ? AND employer_id = ?
            """, (job_id, employer_id))

            if cursor.rowcount:
                connection.commit()
                print("\nJob vacancy reopened successfully!")
            else:
                print("\nJob not found.")

        elif choice == "5":

            job_id = input("Enter Job ID to delete: ")

            cursor.execute("""
                SELECT id FROM jobs
                WHERE id = ? AND employer_id = ?
            """, (job_id, employer_id))

            if cursor.fetchone():

                confirm = input(
                    "Are you sure you want to delete this job? (yes/no): "
                )

                if confirm.lower() == "yes":

                    cursor.execute(
                        "DELETE FROM applications WHERE job_id = ?",
                        (job_id,)
                    )

                    cursor.execute(
                        "DELETE FROM saved_jobs WHERE job_id = ?",
                        (job_id,)
                    )

                    cursor.execute("""
                        DELETE FROM jobs
                        WHERE id = ? AND employer_id = ?
                    """, (job_id, employer_id))

                    connection.commit()
                    print("\nJob deleted successfully!")

                else:
                    print("\nDeletion cancelled.")

            else:
                print("\nJob not found.")

        elif choice == "6":

            connection.close()
            print("\nReturning to Employer Dashboard...")
            break

        else:
            print("\nInvalid choice. Try again.")

        connection.close()
