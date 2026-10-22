# Classical (boring way)
squares = []
for n in range(10):
    squares.append(n ** 2)

print(squares)
print()

# Use map
squares = list(map(lambda n: n**2, range(10)))
print(squares)
print()

# Comprehension (the pythonista way)
print([n**2 for n in range(10)])