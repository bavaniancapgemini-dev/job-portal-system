import sqlite3

connection = sqlite3.connect("job_portal.db")
cursor = connection.cursor()

print("\n========== REGISTERED EMPLOYERS ==========")

cursor.execute("""
    SELECT id, company_name, email
    FROM employers
""")

for employer in cursor.fetchall():
    print(employer)

print("\n========== ALL POSTED JOBS ==========")

cursor.execute("""
    SELECT id, employer_id, title, company_name
    FROM jobs
""")

for job in cursor.fetchall():
    print(job)

connection.close()