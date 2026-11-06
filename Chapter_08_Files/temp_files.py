from tempfile import TemporaryDirectory, NamedTemporaryFile

# Create a temporary directory and a temporary file within it in cwd
with TemporaryDirectory(dir=".") as td:
    print("Temporary directory: ", td)
    with NamedTemporaryFile(dir=td) as t:
        name = t.name
        print(name)