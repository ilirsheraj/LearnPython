# Let's call a comprehension without defining A and then check global scope
ex1 = [A for A in range(5)]
print(ex1)

try:
    print(A)
except NameError:
    print("A does not exist in global scope")

# But it works fine with for-loop
s = 0
for A in range(5):
    s += A
print(s)
print(A)
print()
print(globals())