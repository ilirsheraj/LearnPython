# set is mutable, frozenset is immutable
# empty set
small_primes = set()
print(small_primes)
small_primes.add(2)
small_primes.add(3)
small_primes.add(5)
print(small_primes)

small_primes.add(1)
print(small_primes)
small_primes.remove(1)
print(small_primes)

print(3 in small_primes)
print(4 in small_primes)
print()
print("Add 3 to small primes and see what happens")
small_primes.add(3)
print(small_primes)

bigger_primes = set([5, 7, 11, 13])
print(bigger_primes)

print("Union of small and bigger primes")
print(small_primes | bigger_primes)
print("Intersection of small and bigger primes")
print(small_primes & bigger_primes)

print("Difference between small and bigger primes")
print(small_primes - bigger_primes)
print("Difference between bigger and small primes")
print(bigger_primes - small_primes)
print()

print("Lets work with frozen sets")
small_primes = frozenset([2, 3, 5, 7])
print(small_primes)
bigger_primes = frozenset([5, 7, 11])
print(bigger_primes)
print("Lets try to change immutable object")
try:
    small_primes.add(11)
except AttributeError:
    print(f"{type(small_primes)}")

print(small_primes & bigger_primes)
