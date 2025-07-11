#!/usr/bin/env python3

import os
import time
def create_fold():

    fold_name = "testing_folder"
    fold_path = "/home/ubuntu/"
    path = os.path.join(fold_path, fold_name)

    if os.path.exists(path):
        print("already exsits", path)
    else:
         os.mkdir(path)
         print("creating folder...")
         time.sleep(1)
         print("created")

create_fold()
