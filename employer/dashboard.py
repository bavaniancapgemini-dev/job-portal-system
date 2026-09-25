def employer_dashboard(employer):
    while True:
        print("\n===================================")
        print("        EMPLOYER DASHBOARD")
        print("===================================")
        print("1. View Company Profile")
        print("2. Post Job")
        print("3. View Posted Jobs")
        print("4. Logout")
        print("===================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_company_profile(employer)

        elif choice == "2":
            print("\nJob posting feature coming soon.")

        elif choice == "3":
            print("\nPosted jobs feature coming soon.")

        elif choice == "4":
            print("\nLogged out successfully.")
            break

        else:
            print("\nInvalid choice. Please try again.")


def view_company_profile(employer):
    print("\n===================================")
    print("        COMPANY PROFILE")
    print("===================================")
    print("Employer ID :", employer[0])
    print("Company     :", employer[1])
    print("Email       :", employer[2])
    print("Industry    :", employer[3])
    print("===================================")