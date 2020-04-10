from pathlib import Path

# Absolute Path
# example : C:\Program Files\JetBrains
# Relative Path

# path = Path()  # denotes current directory
# path = Path("emails")
# print(path.exists())  # returns boolean indicating whether the path exists or not
# print(path.mkdir())   # makes a new directory named "emails" to current directory
# print(path.rmdir())   # removes the directory name "emails" from current directory

path = Path()
py_files = path.glob("*.py")  # "*" means all files , ".py" indicates extension , we can use path.glob("*") to get all files with any extension

for file in py_files:
    print(file)

