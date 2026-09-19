from itertools import permutations

perms = list(permutations("ABC"))

for i in perms:
    print(i)

print()

perms2 = list(permutations([1,2,3,4]))

for i in perms2:
    print(i)
