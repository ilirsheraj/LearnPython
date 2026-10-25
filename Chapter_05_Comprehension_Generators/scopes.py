# Let's explore the scope
A = 100

ex1 = [A for A in range(5)]
print(ex1)
print(f"The value of A is {A}")
print()

ex2 = list(A for A in range(5))
print(ex2)
print(f"The value of A is {A}")
print()

ex3 = {A: 2 * A for A in range(5)}
print(ex3)
print(f"The value of A is {A}")

ex4 = {A for A in range(5)}
print(ex4)
print(f"The value of A is {A}")

# Now for-loop
s = 0
for A in range(5):
    s += A

print(s)
print(f"The value of A is {A}")