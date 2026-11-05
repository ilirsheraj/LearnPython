fh = open("fear.txt", "rt")

# To make sure the file is closed no matter what
try:
    for line in fh.readlines():
        print(line.strip())

finally:
    fh.close()