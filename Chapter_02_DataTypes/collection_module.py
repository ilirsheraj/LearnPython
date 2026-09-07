from collections import namedtuple, defaultdict, ChainMap
from enum import Enum

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
print("-" * 50)
print()

# Explore ChainMap
default_connection = {"host": "localhost", "port": 4567}
connection = {"port": 5678}
print(f"The default connection is {default_connection}")
print(f"The connection is {connection}")

conn = ChainMap(connection, default_connection)
print(conn["port"])
print(conn["host"])
print(conn.maps)

conn["host"] = "packtpub.com"
print(conn.maps)

del conn["port"]
print(conn.maps)
print(conn["port"])
print(dict(conn))
print("-" * 50)
print()

# Explore Enum
class TrafficLight(Enum):
    GREEN = 1
    YELLOW = 2
    RED = 4

print(TrafficLight.GREEN)
print(TrafficLight.GREEN.value)
print(TrafficLight(1))
print(TrafficLight(4))



