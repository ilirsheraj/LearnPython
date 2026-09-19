items = [0, None, 0.0, True, 0, 7]

found = False
if any(items):
    found = True

if found:
    print("At least one item evaluates to True")
else:
    print("All items evaluate to False")