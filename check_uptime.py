#!/usr/bin/env python3

import subprocess

def check_uptime():

    uptime = subprocess.run(['uptime'], capture_output=True, text=True)

    print(uptime.stdout.strip())

def check_date():
    date = subprocess.run(['date'], capture_output=True, text=True)
    print(date.stdout.strip())

check_uptime()
check_date()
