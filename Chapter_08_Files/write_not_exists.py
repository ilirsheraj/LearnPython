# Create a file only if it doesn't exist already
with open("write_x.txt", "x") as fw:
    fw.write("Writing line 1")

# Now it will fail because the file already exists
try:
    with open("write_x.txt", "x") as fw:
        fw.write("Writing line 2")

except FileExistsError:
    print()