# Many different ways to create a dictionary
a = dict(A=1, Z=-1)
print(a)

# My favorite
b = {"A": 1, "Z": -1}
print(b)

# My second favorite
c = dict(zip(["A", "Z"], [1,-1]))

d = dict([("A", 1), ("Z", -1)])
print(d)

e = dict({"A": 1, "Z": -1})
print(e)

print(a == b == c == d == e)