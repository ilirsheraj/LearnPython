import shutil
from os import mkdir
from pathlib import Path

base_path = Path("ops_example")

# Perform cleanup
if base_path.exists() and base_path.is_dir():
    shutil.rmtree(base_path)

# Create the directory called "ops_example"
base_path.mkdir()

# Create subdirectory A within ops_example
# Create 2 subdirectories, B and C within A
path_b = base_path / "A" / "B"
path_c = base_path / "A" / "C"
path_d = base_path / "A" / "D"

# Create A and B instantly
path_b.mkdir(parents=True)
# No need for parents=True because A has already been created
path_c.mkdir()

# Add 3 files ex1-3 in B
for filename in ("ex1.txt", "ex2.txt", "ex3.txt"):
    # pathlib takes care of the OS here!
    with open(path_b / filename, "w") as stream:
        stream.write(f"Some contents here in {filename}\n")

# Move directory B and its contents to D
# This is cool, Python trying to emulate terminal :)
shutil.move(path_b, path_d)

# Automatically rename the files
ex1 = path_d / "ex1.txt"
ex1.rename(ex1.parent / "ex1.renamed.txt")