import shutil
from pathlib import Path

base_path = Path("ops_example")

# Perform cleanup
if base_path.exists() and base_path.is_dir():
    shutil.rmtree(base_path)

# Create the directory
base_path.mkdir()