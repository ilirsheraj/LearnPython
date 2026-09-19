# Only True and 7 evaluate to True, rest false
items = [0, None, 0.0, True, 0, 7]

# Set the "Flag" to false by default. It will turn to True if it fulfills the
# condition
found = False
for item in items:
    print("Scanning item", item)
    # we could say if item == True, but its not necessary
    if item:
        found = True
        break

if found:
    print("At least one item evaluates to True")
else:
    print("All items evaluate to False")
