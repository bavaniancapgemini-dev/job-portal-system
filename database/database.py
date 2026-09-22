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

    connection.commit()
    connection.close()

    print("Database initialized successfully.")


if __name__ == "__main__":
    create_database()