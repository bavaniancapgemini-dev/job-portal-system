
import sqlite3


def create_database():
    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    # JOB SEEKERS TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS job_seekers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            skills TEXT
        )
    """)

    # EMPLOYERS TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            industry TEXT
        )
    """)

    # JOBS TABLE
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
            is_open INTEGER NOT NULL DEFAULT 1,
            FOREIGN KEY (employer_id) REFERENCES employers(id)
        )
    """)

    # APPLICATIONS TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_id INTEGER NOT NULL,
            job_seeker_id INTEGER NOT NULL,
            status TEXT NOT NULL DEFAULT 'Applied',
            FOREIGN KEY (job_id) REFERENCES jobs(id),
            FOREIGN KEY (job_seeker_id) REFERENCES job_seekers(id)
        )
    """)

    # SAVED JOBS TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS saved_jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_seeker_id INTEGER NOT NULL,
            job_id INTEGER NOT NULL,
            FOREIGN KEY (job_seeker_id) REFERENCES job_seekers(id),
            FOREIGN KEY (job_id) REFERENCES jobs(id),
            UNIQUE(job_seeker_id, job_id)
        )
    """)

    # ADMINS TABLE - NEW
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS admins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()

    print("Database initialized successfully.")


if __name__ == "__main__":
    create_database()
