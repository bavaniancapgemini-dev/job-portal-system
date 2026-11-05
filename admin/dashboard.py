
from admin.user_management import (
    view_all_job_seekers,
    view_all_employers,
    search_users,
    delete_user_account
)

from admin.job_management import (
    view_all_jobs,
    delete_job_as_admin
)

from admin.application_management import (
    view_all_applications,
    application_statistics
)

from admin.platform_statistics import view_platform_statistics

from admin.reports import (
    export_job_seekers,
    export_employers,
    export_jobs,
    export_applications
)

from admin.backup import (
    backup_database,
    view_database_backups
)


def admin_dashboard(admin):

    while True:

        print("\n===================================")
        print("          ADMIN DASHBOARD")
        print("===================================")

        print("Welcome,", admin[1])

        print("\nUSER MANAGEMENT")
        print("1. View All Job Seekers")
        print("2. View All Employers")
        print("3. Search Users")
        print("4. Delete User Account")

        print("\nJOB MANAGEMENT")
        print("5. View All Jobs")
        print("6. Delete Job Posting")

        print("\nAPPLICATION MANAGEMENT")
        print("7. View All Applications")
        print("8. Application Statistics")

        print("\nANALYTICS")
        print("9. Platform Statistics")

        print("\nREPORTS")
        print("10. Export Job Seeker Report")
        print("11. Export Employer Report")
        print("12. Export Job Report")
        print("13. Export Application Report")

        print("\nDATABASE MANAGEMENT")
        print("14. Create Database Backup")
        print("15. View Database Backups")

        print("\n16. Logout")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            view_all_job_seekers()

        elif choice == "2":
            view_all_employers()

        elif choice == "3":
            search_users()

        elif choice == "4":
            delete_user_account()

        elif choice == "5":
            view_all_jobs()

        elif choice == "6":
            delete_job_as_admin()

        elif choice == "7":
            view_all_applications()

        elif choice == "8":
            application_statistics()

        elif choice == "9":
            view_platform_statistics()

        elif choice == "10":
            export_job_seekers()

        elif choice == "11":
            export_employers()

        elif choice == "12":
            export_jobs()

        elif choice == "13":
            export_applications()

        elif choice == "14":
            backup_database()

        elif choice == "15":
            view_database_backups()

        elif choice == "16":
            print("\nAdmin logged out successfully!")
            break

        else:
            print("\nInvalid choice. Please try again.")
