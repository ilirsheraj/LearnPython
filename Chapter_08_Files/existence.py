# Instead of os.path, we now use pathlib
from pathlib import Path

# fear.txt was created previously, and it is in the current working directory
p = Path("fear.txt")
path = p.parent.absolute()

# Print the absolute path where fear.txt is located
print(path)

# Check if fear.txt is a file
print(p.is_file())
# True
print(path.is_file())
print(path.is_dir())