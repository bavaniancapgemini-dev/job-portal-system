from job_seeker.registration import register_job_seeker
from job_seeker.login import login_job_seeker
from employer.registration import register_employer
from employer.login import login_employer


def main_menu():
    while True:
        print("\n===================================")
        print("         JOB PORTAL SYSTEM")
        print("===================================")
        print("1. Job Seeker Registration")
        print("2. Job Seeker Login")
        print("3. Employer Registration")
        print("4. Employer Login")
        print("5. Admin")
        print("6. Exit")
        print("===================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_job_seeker()

        elif choice == "2":
            login_job_seeker()

        elif choice == "3":
            register_employer()

        elif choice == "4":
            login_employer()

        elif choice == "5":
            print("\nAdmin section selected.")

        elif choice == "6":
            print("\nThank you for using Job Portal System!")
            break

        else:
            print("\nInvalid choice. Please try again.")

main_menu()