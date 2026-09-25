import sqlite3
from employer.dashboard import employer_dashboard


def login_employer():
    print("\n===================================")
    print("          EMPLOYER LOGIN")
    print("===================================")

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, company_name, email, industry
        FROM employers
        WHERE email = ? AND password = ?
    """, (email, password))

    employer = cursor.fetchone()

    connection.close()

    if employer:
        print("\nLogin Successful!")
        print("Welcome,", employer[1])
        
        employer_dashboard(employer)

        return employer

    else:
        print("\nInvalid email or password.")
        return None