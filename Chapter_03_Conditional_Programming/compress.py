from itertools import compress

# compress is extremely useful!!!

data = range(10)

# 0 is even, so be careful
even_selector = [1, 0] * 10
odd_selector = [0, 1] * 10

even_numbers = list(compress(data, even_selector))
odd_numbers = list(compress(data, odd_selector))

print(f"The original data list is: {list(data)}")
print(f"Even Selector is: {even_selector}")
print(f"Odd Selector is {odd_selector}")
print(f"List of even numbers: {even_numbers}")
print(f"List of odd numbers: {odd_numbers}")
