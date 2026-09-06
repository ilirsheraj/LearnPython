# Some dictionary methods
d = {}
print(d)

d["a"] = 1
print(d)

d["b"] = 2
print(d)

print(d["a"])
print(d)

del d["a"]
print(d)

d["c"] = 3
print(d)

print("c" in d)
print(3 in d)
print("e" in d)
d.clear()
print(d)

# Start a new one
d = dict(zip("hello", range(5)))
print(d)

print(d.keys())
print(d.values())
print(d.items())

print(3 in d.values())
print("h" in d.keys())
print(("o", 3) in d.items())
print(("o", 4) in d.items())

# More methods
print(d)

# Remove the last item
print(d.popitem())
print(d)

# Remove l specifically
print(d.pop("l"))
print(d)

# Update
d.update({"another": "value"})
d.update(a=13)
print(d)

print(d.get("a"))
print(d.get("a", 117))
print(d.get("b", 177))

# Last Piece
d = {}
print(d)

d.setdefault("a", 1)
print(d)
d.setdefault("a", 2)
print(d)

d = {}
d.setdefault("a", {}).setdefault("b", []).append(1)
print(d)

# Union Operator
d = {"a": "A", "b": "B"}
print(d)
e = {"b": 8, "c": "C"}
print(e)

print(d | e)
print(e | d)

# Another way is unpacking
print({**d, **e})
print({**e, **d})
