from job_seeker.application import apply_for_job
from job_seeker.saved_jobs import (
    save_job,
    view_saved_jobs,
    remove_saved_job
)
from job_seeker.application_reports import export_application_report



def job_seeker_dashboard(user):
    while True:
        print("\n===================================")
        print("       JOB SEEKER DASHBOARD")
        print("===================================")
        print("1. View Profile")
        print("2. Update Profile")
        print("3. Search Jobs")
        print("4. Apply for Job")
        print("5. My Applications")
        print("6. View Job Details")
        print("7. Withdraw Job Application")
        print("8. Save Job to Favorites")
        print("9. View Saved Jobs")
        print("10. Remove Saved Job")
        print("11. Export Application Report")
        print("12. Logout")
        print("===================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_profile(user)
        
        elif choice == "2":
            update_profile(user)

        elif choice == "3":
            search_jobs()

        elif choice == "4":
            apply_for_job(user)

        elif choice == "5":
            view_my_applications(user)

        elif choice == "6":
            view_job_details(user)

        elif choice == "7":
            withdraw_application(user)

        elif choice == "8":
            save_job(user)
            
        elif choice == "9":
            view_saved_jobs(user)
            
        elif choice == "10":
            remove_saved_job(user)
            
        elif choice == "11":
            export_application_report(user)
            
        elif choice == "12":
            break

        else:
            print("\nInvalid choice. Please try again.")


def view_profile(user):
    print("\n===================================")
    print("           MY PROFILE")
    print("===================================")
    print("User ID :", user[0])
    print("Name    :", user[1])
    print("Email   :", user[2])
    print("Skills  :", user[3])
    print("===================================")
    
def search_jobs():
    import sqlite3

    print("\n===================================")
    print("          SEARCH JOBS")
    print("===================================")

    keyword = input("Enter job title or skill: ")
    location = input("Enter location: ")
    job_type = input("Enter job type: ")

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    query = """
        SELECT id, title, company_name, location,
               salary, job_type, skills
        FROM jobs
        WHERE title LIKE ?
          AND location LIKE ?
          AND job_type LIKE ?
    """

    cursor.execute(query, (
        "%" + keyword + "%",
        "%" + location + "%",
        "%" + job_type + "%"
    ))

    jobs = cursor.fetchall()

    connection.close()

    if not jobs:
        print("\nNo jobs found matching your search.")
        return

    print("\nJobs Found:")
    print("-----------------------------------")

    for job in jobs:
        print("\nJob ID    :", job[0])
        print("Title     :", job[1])
        print("Company   :", job[2])
        print("Location  :", job[3])
        print("Salary    :", job[4])
        print("Job Type  :", job[5])
        print("Skills    :", job[6])
        print("-----------------------------------")
    
def view_my_applications(user):
    import sqlite3

    print("\n===================================")
    print("         MY APPLICATIONS")
    print("===================================")

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            applications.id,
            jobs.title,
            jobs.company_name,
            jobs.location,
            applications.status
        FROM applications
        JOIN jobs
            ON applications.job_id = jobs.id
        WHERE applications.job_seeker_id = ?
    """, (user[0],))

    applications = cursor.fetchall()

    connection.close()

    if not applications:
        print("\nYou have not applied for any jobs yet.")
        return

    for application in applications:
        print("\n-----------------------------------")
        print("Application ID :", application[0])
        print("Job Title      :", application[1])
        print("Company        :", application[2])
        print("Location       :", application[3])
        print("Status         :", application[4])
        print("-----------------------------------")
        
def update_profile(user):
    import sqlite3

    print("\n===================================")
    print("          UPDATE PROFILE")
    print("===================================")

    print("Current Name   :", user[1])
    print("Current Skills :", user[3])

    print("\nEnter new details.")
    print("Press Enter to keep the current value.")

    new_name = input("New name: ")
    new_skills = input("New skills: ")

    if new_name == "":
        new_name = user[1]

    if new_skills == "":
        new_skills = user[3]

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE job_seekers
        SET name = ?, skills = ?
        WHERE id = ?
    """, (new_name, new_skills, user[0]))

    connection.commit()
    connection.close()

    print("\nProfile updated successfully!")
    print("-----------------------------------")
    print("Name   :", new_name)
    print("Skills :", new_skills)
    print("-----------------------------------")
    
def view_job_details(user):

    import sqlite3

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, title, company_name, location,
               salary, job_type, description, skills
        FROM jobs
    """)

    jobs = cursor.fetchall()

    if not jobs:
        print("\nNo jobs available.")
        connection.close()
        return

    print("\n========== AVAILABLE JOBS ==========")

    for job in jobs:
        print(f"\nJob ID: {job[0]}")
        print(f"Title: {job[1]}")
        print(f"Company: {job[2]}")
        print(f"Location: {job[3]}")

    try:
        job_id = int(input("\nEnter Job ID to view details: "))
    except ValueError:
        print("Please enter a valid Job ID.")
        connection.close()
        return

    cursor.execute("""
        SELECT id, title, company_name, location,
               salary, job_type, description, skills
        FROM jobs
        WHERE id = ?
    """, (job_id,))

    job = cursor.fetchone()

    if job:
        print("\n========== JOB DETAILS ==========")
        print("Job ID:", job[0])
        print("Title:", job[1])
        print("Company:", job[2])
        print("Location:", job[3])
        print("Salary:", job[4])
        print("Job Type:", job[5])
        print("Description:", job[6])
        print("Required Skills:", job[7])
        print("=================================")

    else:
        print("\nInvalid Job ID.")

    connection.close()
    
def withdraw_application(user):

    import sqlite3

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    job_seeker_id = user[0]

    cursor.execute("""
        SELECT applications.id, jobs.title,
               jobs.company_name, applications.status
        FROM applications
        JOIN jobs ON applications.job_id = jobs.id
        WHERE applications.job_seeker_id = ?
    """, (job_seeker_id,))

    applications = cursor.fetchall()

    if not applications:
        print("\nYou have not applied for any jobs.")
        connection.close()
        return

    print("\n========== YOUR APPLICATIONS ==========")

    for application in applications:
        print("\nApplication ID:", application[0])
        print("Job Title:", application[1])
        print("Company:", application[2])
        print("Status:", application[3])

    try:
        application_id = int(input("\nEnter Application ID to withdraw: "))
    except ValueError:
        print("Please enter a valid ID.")
        connection.close()
        return

    cursor.execute("""
        SELECT id, status
        FROM applications
        WHERE id = ? AND job_seeker_id = ?
    """, (application_id, job_seeker_id))

    application = cursor.fetchone()

    if application:
        if application[1] in ("Selected", "Rejected"):
            print("\nYou cannot withdraw an application that is already Selected or Rejected.")
        else:
            confirm = input("Are you sure you want to withdraw? (yes/no): ").lower()

            if confirm == "yes":
                cursor.execute("""
                    DELETE FROM applications
                    WHERE id = ? AND job_seeker_id = ?
                """, (application_id, job_seeker_id))

                connection.commit()
                print("\nApplication withdrawn successfully!")

            else:
                print("\nWithdrawal cancelled.")

    else:
        print("\nInvalid Application ID.")

    connection.close()
