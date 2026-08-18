a = [1, 2, 1, 3]
print(a)
# add a number at the end
a.append(13)
print(a)
# Find out how many 1's are there
print(a.count(1))

# Add two elements at once
a.extend([5, 17])
print(a)

# FInd the index of number 13
print(a.index(13))

# Insert 17 on position 0
a.insert(0,17)
print(a)

# Remove the last element
print(a.pop())
print(a)

# Remove element at position 3
a.pop(3)
print(a)

# Remove specific value: 17
a.remove(17)
print(a)

# Reverse the element order
a.reverse()
print(a)

# Sort the list in place (mutate)
a.sort()
print(a)

# Delete everything
a.clear()
print(a)
#####################################################
print("We can work the same way with strings")
a = "hello"
print(a)
a = list(a)
print(a)

# Create heterogenous list
a.append(100)
print(a)
a.extend((1,2,3))
print(a)
a.extend("...")
print(a)
print()
###############################################
# Some more operations
print("Some math operations with lists")
a = [1, 3, 5, 7]
print(a)
print(min(a))
print(max(a))
print(sum(a))

from math import prod
print(prod(a))
print(len(a))

b = [6, 7, 8]
print(a + b)
print(a*2)