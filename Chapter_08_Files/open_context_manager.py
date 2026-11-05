# use with: closed automatically
with open("fear.txt") as fh:
    for line in fh:
        print(line.strip())