from math import sqrt

# This function finds pyhtagoren triplest within a range of numbers defined by mx
# for example (3, 4, 5)
mx = 10
triples = [(a, b, sqrt(a**2 + b**2)) for a in range(1, mx) for b in range(a, mx)]
# print(triples)

# Now comes the filtering keeping only integers
triples = list(filter(lambda triples: triples[2].is_integer(), triples))
print(triples)
print()
# # Make the number integer without floating point
triples = list(map(lambda triple: triple[:2] + (int(triple[2]),), triples))
print(triples)