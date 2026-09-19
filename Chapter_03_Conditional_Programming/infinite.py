# Part of iterator tools
from itertools import count

# n will grow from 5 to infinity by adding 3 every time
for n in count(5, 3):
    # Break it here otherwise it goes on forever
    if n > 20:
        break

    print(n, end = ", ")
