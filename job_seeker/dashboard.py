def job_seeker_dashboard(user):
    while True:
        print("\n===================================")
        print("       JOB SEEKER DASHBOARD")
        print("===================================")
        print("1. View Profile")
        print("2. Search Jobs")
        print("3. Apply for Job")
        print("4. Logout")
        print("===================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_profile(user)

        elif choice == "2":
            search_jobs()

        elif choice == "3":
            print("\nJob application feature coming soon.")

        elif choice == "4":
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