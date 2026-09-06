from collections import namedtuple, defaultdict

Vision = namedtuple("Vision", ["left", "right"])
vision = Vision(left=9.5, right=8.8)
print(vision)
print(vision.left)
print(vision[0])
print(vision.right)
print(vision[1])

# Now make the changes
Vision = namedtuple("Vision", ["left", "combined", "right"])
vision = Vision(left=9.5, combined=9.2, right=8.8)
print(vision)
print(vision.left)
print(vision.right)
print(vision.combined)
print("-" * 50)
# Default dictionary
d = defaultdict(int) # value 0
print(d)
d["age"] += 1
print(d)