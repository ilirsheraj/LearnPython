# Try map
print(map(lambda a: a, range(5)))
print()

print(list(map(lambda *a: a, range(3))))
print()

print(list(map(lambda *a: a, range(3), "abc")))
print()

print(list(map(lambda *a: a, range(3), "abc", range(4,7))))
print()

print(list(map(lambda *a: a, (), "abc")))
print()

print(list(map(lambda *a: a, (1,2), "abc")))
print()

print(list(map(lambda *a: a, (1, 2, 3, 4), "abc")))