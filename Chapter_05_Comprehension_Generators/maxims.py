# calculate the element-wise maximum among sequences
a = [5, 9, 2, 4, 7]
b = [3, 7, 1, 9, 2]
c = [6, 8, 0, 5, 3]

maxs = map(lambda n: max(*n), zip(a, b, c))
# Another way without using zip at all
max2 = map(lambda *n: max(*n), a, b, c)

print(a)
print(b)
print(c)
print()
print(list(maxs))
print(list(max2))