from pathlib import Path

p = Path("fear.txt")

print(p.absolute())
print(p.name)
print()
# Up to, but not including file name, just the folder its found in
print(p.parent.absolute())
print(p.suffix)
print(p.parts)
print()

# Break the path into directories
print(p.absolute().parts)

print()
readme_path = p.parent / ".." / ".." / "README.rst"
print(readme_path.absolute())
print(readme_path.resolve())