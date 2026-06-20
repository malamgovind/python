import os

folder = "projects"

if not os.path.exists(folder):
    os.mkdir(folder)

print("Folder Created")

if os.path.exists(folder):
    os.rmdir(folder)

print("Folder Deleted")


# projects folder નથી
#         ↓
# os.mkdir("projects")
#         ↓
# projects folder બને

#         ↓
# os.rmdir("projects")
#         ↓
# projects folder delete થાય