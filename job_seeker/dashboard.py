def job_seeker_dashboard(user):
    while True:
        print("\n===================================")
        print("       JOB SEEKER DASHBOARD")
        print("===================================")
        print("1. View Profile")
        print("2. Search Jobs")
        print("3. Apply for Job")
        print("4. Logout")
        print("===================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_profile(user)

        elif choice == "2":
            print("\nJob search feature coming soon.")

        elif choice == "3":
            print("\nJob application feature coming soon.")

        elif choice == "4":
            print("\nLogged out successfully.")
            break

        else:
            print("\nInvalid choice. Please try again.")


def view_profile(user):
    print("\n===================================")
    print("           MY PROFILE")
    print("===================================")
    print("User ID :", user[0])
    print("Name    :", user[1])
    print("Email   :", user[2])
    print("Skills  :", user[3])
    print("===================================")