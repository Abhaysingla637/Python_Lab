import os
import sys

# 1. Get the current directory
base_dir = os.getcwd()
print("Current Working Directory:", base_dir)

# 2. Create workspace
workspace_path = os.path.join(base_dir, "workspace")

if not os.path.isdir(workspace_path):
    os.makedirs(workspace_path)
    print("\nWorkspace created.")
else:
    print("\nWorkspace already exists.")

# 3. Move to workspace
os.chdir(workspace_path)
print("Working inside:", os.getcwd())

# 4. Display text files
print("\nAvailable Text Files:")
text_files = []

for item in os.listdir():
    if item.endswith(".txt"):
        text_files.append(item)

if text_files:
    for item in text_files:
        print(item)
else:
    print("No text files found.")

# 5. Take filename from command line
if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = "log.txt"

if not file_name.endswith(".txt"):
    file_name += ".txt"

# 6. Create and read the file
file_path = os.path.join(workspace_path, file_name)

try:
    if not os.path.isfile(file_path):
        with open(file_path, "w") as f:
            f.write("Log file created successfully.\n")
        print("\nCreated:", file_name)

    with open(file_path, "r") as f:
        data = f.read()

    print("\nFile Content:")
    print(data)

except PermissionError:
    print("Error: Permission denied.")

except Exception as error:
    print("Error:", error)

# 7. Display final directory
print("\nFinal Directory:", os.getcwd())