
import sqlite3
import os
from datetime import datetime
from admin.activity_logs import log_admin_activity


def backup_database(admin_name):

    source_database = "job_portal.db"

    if not os.path.exists(source_database):
        print("\nDatabase file not found!")
        return

    os.makedirs("database_backups", exist_ok=True)

    backup_filename = (
        "job_portal_backup_"
        + datetime.now().strftime("%Y%m%d_%H%M%S")
        + ".db"
    )

    backup_path = os.path.join(
        "database_backups",
        backup_filename
    )

    try:

        source = sqlite3.connect(source_database)
        destination = sqlite3.connect(backup_path)

        source.backup(destination)

        destination.close()
        source.close()

        print("\n===================================")
        print("       DATABASE BACKUP SUCCESSFUL")
        print("===================================")
        print("Backup saved at:", backup_path)
        log_admin_activity(
            admin_name,
            "Database Backup",
            "Created database backup: " + backup_filename
        )

    except sqlite3.Error as error:

        print("\nBackup failed:", error)


def view_database_backups():

    backup_folder = "database_backups"

    print("\n========== DATABASE BACKUPS ==========")

    if not os.path.exists(backup_folder):
        print("\nNo backups available.")
        return

    backups = sorted(os.listdir(backup_folder), reverse=True)

    if not backups:
        print("\nNo backups available.")
        return

    for index, backup in enumerate(backups, start=1):
        print(f"{index}. {backup}")
