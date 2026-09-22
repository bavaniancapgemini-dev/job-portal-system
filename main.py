from job_seeker.registration import register_job_seeker
from job_seeker.login import login_job_seeker


def main_menu():
    while True:
        print("\n===================================")
        print("         JOB PORTAL SYSTEM")
        print("===================================")
        print("1. Job Seeker Registration")
        print("2. Job Seeker Login")
        print("3. Employer")
        print("4. Admin")
        print("5. Exit")
        print("===================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_job_seeker()

        elif choice == "2":
            login_job_seeker()

        elif choice == "3":
            print("\nEmployer section selected.")

        elif choice == "4":
            print("\nAdmin section selected.")

        elif choice == "5":
            print("\nThank you for using Job Portal System!")
            break

        else:
            print("\nInvalid choice. Please try again.")


main_menu()