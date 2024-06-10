import shutil
import os
import time

path = input("Enter the path : ")

try:
    path = os.path.abspath(path)

    time.sleep(1)
    for local_dir, folder, file in os.walk(path):
        if len(file) > 0:
            for f in file:
                if local_dir == path:
                    continue
                src = os.path.join(local_dir, f)
                dest = os.path.join(path, f)
                shutil.move(src, dest)
    print("Files Successfully Unpacked")
    time.sleep(1)

    while True:
        ch = input("Do you want to delete all the empty folders? (y/n) ").lower()
        if ch == "n":
            exit(0)
        elif ch == "y":
            for local_dir, folder, file in os.walk(path):
                if len(folder) > 0:
                    for f in folder:
                        try:
                            folder_path = os.path.join(local_dir, f)
                            os.rmdir(folder_path)
                        except OSError as e:
                            print(f"Error : {e.strerror}")
            print("Empty folders successfully deleted")
            time.sleep(1)
            exit(0)
        else:
            print("Invalid Input")
except Exception as e:
    print(f"Error occured : {e}")