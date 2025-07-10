#!/usr/bin/env python3

import subprocess
import os
import time

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
    with open(alert_path, "a") as f:
        if usage_percent > 80:
            message = f"🚨 ALERT: Disk usage is {usage_percent}% \n"
            f.write(message)
        else:
            message = f"✅ Disk usage is normal: {usage_percent}% \n"
            f.write(message)
    print("Alert.txt saved with disk info.")
    return True if usage_percent > 80 else False

alert()




