import io

with io.StringIO() as stream:
    stream.write("Learning Python Programming.\n")
    print("Become a Python Ninja!", file=stream)
    contents = stream.getvalue()
    print(contents)