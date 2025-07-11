#!/usr/bin/env python3

import subprocess
import os
import time
import datetime
import shutil
import tarfile

def alert():

#Setup folder and file paths
    alert_folder_path = "/home/ubuntu/diskusage_fold"
    alert_file = "alert.txt"
    alert_path = os.path.join(alert_folder_path, alert_file)

#creating folder
    if not os.path.exists(alert_folder_path):
            os.mkdir(alert_folder_path)
            print("Creating Folder")
    else:
            print("Folder already exist")
    time.sleep(1)


#creating Alerts
    check_alert = subprocess.run(['df', '-h', '/'], capture_output=True, text=True)
    lines = check_alert.stdout.strip().split('\n')
    info = lines[1].split()
    usage_percent = int(info[4].replace('%', ''))

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(alert_path, "a") as f:
        if usage_percent > 80:
            message = f"{timestamp}: 🚨 ALERT: Disk usage is {usage_percent}% Testing cron_jobs \n"
            f.write(message)
        else:
            message = f"{timestamp}: ✅ Disk usage is normal: {usage_percent}% Testing cron_jobs \n"
            f.write(message)
    print("Alert.txt saved with disk info.")
    return True if usage_percent > 80 else False

#############################################################################################################

def archive():

    log_file = "/home/ubuntu/diskusage_fold/"
    log_path = "/home/ubuntu/diskusage_fold/"
    backup_path = os.path.join(log_path, log_file)


    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    archive_name = f"alert_{timestamp}.tar.gz"
    archive_path = os.path.join(backup_path, archive_name)

    with tarfile.open(archive_path, "w:gz") as tar:
        tar.add(log_file, arcname="alert.txt")

    print(f"✅ Logs archived as: {archive_path}.tar.gz")


alert()
archive()
