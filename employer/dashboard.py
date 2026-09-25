from employer.post_job import post_job

def employer_dashboard(employer):
    while True:
        print("\n===================================")
        print("        EMPLOYER DASHBOARD")
        print("===================================")
        print("1. View Company Profile")
        print("2. Post Job")
        print("3. View Posted Jobs")
        print("4. Logout")
        print("===================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_company_profile(employer)

        elif choice == "2":
            post_job(employer)

        elif choice == "3":
            view_posted_jobs(employer)

        elif choice == "4":
            print("\nLogged out successfully.")
            break

        else:
            print("\nInvalid choice. Please try again.")


def view_company_profile(employer):
    print("\n===================================")
    print("        COMPANY PROFILE")
    print("===================================")
    print("Employer ID :", employer[0])
    print("Company     :", employer[1])
    print("Email       :", employer[2])
    print("Industry    :", employer[3])
    print("===================================")
    
def view_posted_jobs(employer):
    import sqlite3

    print("\n===================================")
    print("          MY POSTED JOBS")
    print("===================================")

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, title, location, salary, job_type, description, skills
        FROM jobs
        WHERE employer_id = ?
    """, (employer[0],))

    jobs = cursor.fetchall()

    connection.close()

    if not jobs:
        print("\nYou have not posted any jobs yet.")
        return

    for job in jobs:
        print("\n-----------------------------------")
        print("Job ID      :", job[0])
        print("Job Title   :", job[1])
        print("Location    :", job[2])
        print("Salary      :", job[3])
        print("Job Type    :", job[4])
        print("Description :", job[5])
        print("Skills      :", job[6])
        print("-----------------------------------")