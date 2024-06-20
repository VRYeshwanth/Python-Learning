import os
import shutil
import time

videos = [".mp4", ".avi", ".mkv"]
images = [".png", ".jpeg", ".jpg", ".gif", ".ico"]
documents = [".txt", ".docx", ".pptx", ".xlsx", ".doc", ".ppt"]
pdf = [".pdf"]
executables = [".exe"]

path = input("Enter the path : ")
path = rf"{path}"

try:
    os.makedirs(fr"{path}\Videos")
    os.makedirs(fr"{path}\Images")
    os.makedirs(fr"{path}\PDF")
    os.makedirs(fr"{path}\Documents")
    os.makedirs(fr"{path}\Executables")
    os.makedirs(fr"{path}\Others")
except Exception as e:
    pass

files = os.listdir(path)
for file in files:
    file_name, extension = os.path.splitext(file)
    
    if extension.lower() in videos:
        if os.path.isfile(fr"{path}\{file}"):
            shutil.move(fr"{path}\{file}", fr"{path}\Videos")
    if extension.lower() in images:
        if os.path.isfile(fr"{path}\{file}"):
            shutil.move(fr"{path}\{file}", fr"{path}\Images")
    if extension.lower() in documents:
        if os.path.isfile(fr"{path}\{file}"):
            shutil.move(fr"{path}\{file}", fr"{path}\Documents")
    if extension.lower() in pdf:
        if os.path.isfile(fr"{path}\{file}"):
            shutil.move(fr"{path}\{file}", fr"{path}\PDF")
    if extension.lower() in executables:
        if os.path.isfile(fr"{path}\{file}"):
            shutil.move(fr"{path}\{file}", fr"{path}\Executables")
    
    else:
        if os.path.isfile(fr"{path}\{file}"):
            shutil.move(fr"{path}\{file}", fr"{path}\Others")

time.sleep(1)
print("Files successfully sorted")
time.sleep(1)