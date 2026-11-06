import os

for root, dirs, files in os.walk("."):
    abs_root = os.path.abspath(root)
    print(abs_root)

    if dirs:
        print("Directories:")
        for dir_ in dirs:
            print(dir_)
        print()

    if files:
        print("Files:")
        for file_ in files:
            print(file_)
        print()