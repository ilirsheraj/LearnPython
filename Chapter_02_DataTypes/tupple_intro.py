one_element_tuple = (42, )
print(one_element_tuple)
print("-"* 20)

three_element_tuple = (1, 3, 5)
print(three_element_tuple)

a, b, c = 1, 2, 3
print(a, b, c)

# Membership test
print(3 in three_element_tuple)

# Value swapping the old way
a, b = 1, 2
c = a
a = b
b = c
print(a,b)

# With tupples
a, b = 1, 2
a, b = b, a
print(a,b)