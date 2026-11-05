# A simple way to read files in Python
fh = open("fear.txt", "rt")

for line in fh.readlines():
    # print(line)
    # Remove white space and print
    print(line.strip())

# Never forget to close!
fh.close()
