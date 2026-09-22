from job_seeker.registration import register_job_seeker


def main_menu():
    while True:
        print("\n===================================")
        print("         JOB PORTAL SYSTEM")
        print("===================================")
        print("1. Job Seeker")
        print("2. Employer")
        print("3. Admin")
        print("4. Exit")
        print("===================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_job_seeker()

        elif choice == "2":
            print("\nEmployer section selected.")

        elif choice == "3":
            print("\nAdmin section selected.")

        elif choice == "4":
            print("\nThank you for using Job Portal System!")
            break

        else:
            print("\nInvalid choice. Please try again.")


main_menu()