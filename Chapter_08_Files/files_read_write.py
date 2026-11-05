with open("fear.txt") as f:
    # remove white space on the right only (right strip)
    lines = [line.rstrip() for line in f]

# Now write it back to another fear file
with open("fear_copy.txt", "w") as fw:
    fw.write("\n".join(lines))