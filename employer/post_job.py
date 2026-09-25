import sqlite3


def post_job(employer):
    print("\n===================================")
    print("            POST A JOB")
    print("===================================")

    title = input("Enter job title: ")
    location = input("Enter job location: ")
    salary = input("Enter salary: ")
    job_type = input("Enter job type: ")
    description = input("Enter job description: ")
    skills = input("Enter required skills: ")

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO jobs
        (employer_id, title, company_name, location, salary,
         job_type, description, skills)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        employer[0],
        title,
        employer[1],
        location,
        salary,
        job_type,
        description,
        skills
    ))

    connection.commit()
    connection.close()

    print("\nJob posted successfully!")
    print("-----------------------------------")
    print("Job Title :", title)
    print("Company   :", employer[1])
    print("Location  :", location)
    print("Salary    :", salary)
    print("Job Type  :", job_type)
    print("-----------------------------------")