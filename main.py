
from job_seeker.registration import register_job_seeker
from job_seeker.login import login_job_seeker

from employer.registration import register_employer
from employer.login import login_employer

from admin.login import admin_login
from admin.dashboard import admin_dashboard


def main_menu():

    while True:

        print("\n===================================")
        print("         JOB PORTAL SYSTEM")
        print("===================================")

        print("1. Job Seeker Registration")
        print("2. Job Seeker Login")
        print("3. Employer Registration")
        print("4. Employer Login")
        print("5. Admin Login")
        print("6. Exit")

        print("===================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_job_seeker()

        elif choice == "2":
            login_job_seeker()

        elif choice == "3":
            register_employer()

        elif choice == "4":
            login_employer()

        elif choice == "5":

            admin = admin_login()

            if admin:
                admin_dashboard(admin)

        elif choice == "6":

            print("\nThank you for using Job Portal System!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
