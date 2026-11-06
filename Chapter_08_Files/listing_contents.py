from pathlib import Path

p = Path(".")

# List everything in CWD
# similar to ls
for entry in p.glob("*"):
    print("File: " if entry.is_file() else "Directory: ", entry)