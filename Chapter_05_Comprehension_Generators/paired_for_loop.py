items = "ABCD"
pairs = []

for a in range(len(items)):
    for b in range(a, len(items)):
        pairs.append((items[a], items[b]))

print(pairs)

# Use list comprehension
pairs = [(items[a], items[b]) for a in range(len(items)) for b in range(a, len(
    items))]
print(pairs)