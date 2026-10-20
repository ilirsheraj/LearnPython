test = [2, 5, 8, 0, 0, 1, 0]

# By default all False elements are removed
print(list(filter(None, test)))
print()
# Same as above
print(list(filter(lambda x: x, test)))
print()
# Only numbers greater than 4
print(list(filter(lambda x: x > 4, test)))