import sqlite3


def register_employer():
    print("\n===================================")
    print("        EMPLOYER REGISTRATION")
    print("===================================")

    company_name = input("Enter company name: ")
    email = input("Enter company email: ")
    password = input("Create a password: ")
    industry = input("Enter industry: ")

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO employers
            (company_name, email, password, industry)
            VALUES (?, ?, ?, ?)
        """, (company_name, email, password, industry))

        connection.commit()

        print("\nEmployer Registration Successful!")
        print("-----------------------------------")
        print("Company :", company_name)
        print("Email   :", email)
        print("Industry:", industry)
        print("-----------------------------------")

    except sqlite3.IntegrityError:
        print("\nThis company email is already registered.")

    connection.close()