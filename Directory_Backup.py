import os
import shutil

src_dir = input("Enter the path of source directory : ")
dest_dir = input("Enter the path of destination directory : ")

if not os.path.exists(src_dir):
    print(f"\n{src_dir} does not exist\n")
    exit(0)

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)
    print(f"\n{dest_dir} directory created\n")

files = os.listdir(src_dir)
for i,file in enumerate(files):
    src_path = os.path.join(src_dir,file)
    dest_path = os.path.join(dest_dir,file)

    try:
        if os.path.isdir(src_path):
            shutil.copytree(src_path,dest_path)
            print(f"{i+1}){file} Directory copied to {dest_dir}")
        else:
            shutil.copy(src_path,dest_dir)
            print(f"{i+1}){file} copied to {dest_dir}")
    except Exception as e:
        print(f"{i+1}) ERROR : {e}")