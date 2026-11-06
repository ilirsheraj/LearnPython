from collections import Counter
from string import ascii_letters

# Create a list of characters and white space you want to keep
chars = ascii_letters + " "
# print(chars)

def sanitize(s, char):
    """
    It keeps only letters defined in chars
    """
    return "".join(c for c in s if c in char)

def reverse(s):
    """
    Reverses the elements of a list
    """
    return s[::-1]

# Work on file
with open("fear.txt") as stream:
    lines = [line.rstrip() for line in stream]

# Write the mirrored version back in the disk
with open("raef.txt", "w") as stream:
    stream.write("\n".join(reverse(line) for line in lines))

# Let's see the most common words
## Clean non-standard letters and characters and make them lowercase for
# comparison
lines = [sanitize(line, chars) for line in lines]
whole = " ".join(lines)

cnt = Counter(whole.lower().split())
print(cnt.most_common(5))