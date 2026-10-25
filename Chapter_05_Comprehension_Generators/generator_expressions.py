# Regular list
cubes = [k**3 for k in range(10)]
print(cubes)
print(type(cubes))
print()

cubes_gen = (k**3 for k in range(10))
print(cubes_gen)
print()
print(type(cubes_gen))
print()
print(list(cubes_gen))
print()
print(list(cubes_gen))