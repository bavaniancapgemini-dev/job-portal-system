import sqlite3


def create_database():
    connection = sqlite3.connect("job_portal.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS job_seekers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            skills TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            industry TEXT
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employer_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            company_name TEXT NOT NULL,
            location TEXT NOT NULL,
            salary TEXT NOT NULL,
            job_type TEXT NOT NULL,
            description TEXT NOT NULL,
            skills TEXT NOT NULL,
            FOREIGN KEY (employer_id) REFERENCES employers(id)

        )
    """)

    connection.commit()
    connection.close()

    print("Database initialized successfully.")


if __name__ == "__main__":
    create_database()