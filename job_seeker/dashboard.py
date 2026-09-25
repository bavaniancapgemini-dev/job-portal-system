from job_seeker.application import apply_for_job


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
        print("6. Logout")
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
            print("\nLogged out successfully.")
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
    print("            SEARCH JOBS")
    print("===================================")

    keyword = input("Enter job title or skill to search: ")

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, title, company_name, location, salary, job_type, skills
        FROM jobs
        WHERE title LIKE ?
           OR skills LIKE ?
    """, (
        "%" + keyword + "%",
        "%" + keyword + "%"
    ))

    jobs = cursor.fetchall()

    connection.close()

    if not jobs:
        print("\nNo jobs found.")
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