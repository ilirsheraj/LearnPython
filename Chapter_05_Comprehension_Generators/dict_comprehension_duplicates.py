# Duplicate keys not allowed
word = "Hello"
swaps = {c: c.swapcase() for c in word}
print(swaps)
print()

# 2 is skipped
positions = {s: k for k, s in enumerate(word)}
print(positions)
print()

# Make letters value and see all
ind = {s: k for s, k in enumerate(word)}
print(ind)