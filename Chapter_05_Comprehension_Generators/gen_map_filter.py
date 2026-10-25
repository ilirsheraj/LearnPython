# Define the range you are interested in
N = 20
# Two generators returning (n, n**3 tuples
cubes1 = map(lambda n: (n, n**3),
        filter(lambda n: n % 3 == 0 or n % 5 == 0, range(N)))
print(list(cubes1))
print()

# More readable
cubes2 = ((n, n**3) for n in range(N) if n % 3 == 0 or n % 5 == 0)
print(list(cubes2))