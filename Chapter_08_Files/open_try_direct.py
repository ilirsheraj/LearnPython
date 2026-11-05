# rt is the default in python, so no need to specify it
fh = open("fear.txt")

try:
    # Direct iteration on fh
    for line in fh:
        print(line.strip())
finally:
    fh.close()