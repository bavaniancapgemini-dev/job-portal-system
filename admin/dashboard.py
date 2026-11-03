from admin.user_management import (
    view_all_job_seekers,
    view_all_employers
)

from admin.job_management import (
    view_all_jobs,
    delete_job_as_admin
)

from admin.application_management import (
    view_all_applications,
    application_statistics
)


def admin_dashboard(admin):

    while True:

        print("\n===================================")
        print("          ADMIN DASHBOARD")
        print("===================================")

        print("Welcome,", admin[1])

        print("\n1. View All Job Seekers")
        print("2. View All Employers")
        print("3. View All Jobs")
        print("4. Delete Job Posting")
        print("5. View All Applications")
        print("6. Application Statistics")
        print("7. Logout")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            view_all_job_seekers()

        elif choice == "2":
            view_all_employers()

        elif choice == "3":
            view_all_jobs()

        elif choice == "4":
            delete_job_as_admin()

        elif choice == "5":
            view_all_applications()

        elif choice == "6":
            application_statistics()

        elif choice == "7":
            print("\nAdmin logged out successfully!")
            break

        else:
            print("\nInvalid choice. Please try again.")