#!/usr/bin/env python3

import os
import datetime
import time
import subprocess
import shutil

def monitoring():
    folder_path = "/home/ubuntu/monitoring_fold"
    log_file = "moni_log.txt"
    log_path = os.path.join(folder_path, log_file)

    # Ensure the folder exists
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print("📁 Folder created:", folder_path)
    else:
        print("📁 Folder already exists:", folder_path)

    # Delete moni_log.txt if it exists
    if os.path.exists(log_path):
        os.remove(log_path)
        print("🗑️ Removed old moni_log.txt")
    else:
        print("ℹ️ moni_log.txt doesn't exist yet.")

    time.sleep(1)

    # Get uptime and disk info
    uptime = subprocess.run(['uptime'], capture_output=True, text=True)
    disk = subprocess.run(['df', '-h'], capture_output=True, text=True)

    # Save to moni_log.txt
    with open(log_path, "a") as f:
        f.write(uptime.stdout)
        f.write(disk.stdout)

    print("✅ moni_log.txt saved with uptime & disk info.")

monitoring()
