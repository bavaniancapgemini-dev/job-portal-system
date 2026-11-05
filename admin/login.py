
import sqlite3

from admin.security import (
    hash_password,
    verify_password
)


def admin_login():

    print("\n===================================")
    print("           ADMIN LOGIN")
    print("===================================")

    email = input("Enter Admin Email: ").strip().lower()
    password = input("Enter Admin Password: ")

    connection = sqlite3.connect("job_portal.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, email, password
        FROM admins
        WHERE email = ?
    """, (email,))

    admin = cursor.fetchone()

    if not admin:
        connection.close()
        print("\nInvalid Admin Email or Password.")
        return None

    stored_password = admin[3]

    if stored_password.startswith("pbkdf2_sha256$"):

        password_valid = verify_password(
            password,
            stored_password
        )

    else:
        # Support existing accounts with old plaintext passwords.
        password_valid = password == stored_password

        if password_valid:

            new_password_hash = hash_password(password)

            cursor.execute("""
                UPDATE admins
                SET password = ?
                WHERE id = ?
            """, (new_password_hash, admin[0]))

            connection.commit()

    connection.close()

    if password_valid:
        print("\nAdmin Login Successful!")
        print("Welcome,", admin[1])
        return admin

    print("\nInvalid Admin Email or Password.")
    return None
