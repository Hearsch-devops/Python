#!/usr/bin/env python3

import subprocess

def alert():
#creating Alerts
    check_alert = subprocess.run(['df', '-h', '/'], capture_output=True, text=True)
    lines = check_alert.stdout.strip().split('\n')
    info = lines[1].split()

    usage_percent = int(info[4].replace('%', ''))

    if usage_percent > 80:
        print(f"Alert: Disk usage is getting full {usage_percent}% on /")
        return True
    else:
        print(f"Disk usage is normal {usage_percent}%")
        return False
  alert()
