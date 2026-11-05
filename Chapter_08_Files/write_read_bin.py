# first create a binary file: "b" argument
with open("example.bin", "wb") as fw:
    fw.write(b"This is binary data ...")

# Now read binary (rb)
with open("example.bin", "rb") as f:
    print(f.read())