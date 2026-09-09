# Simple for-loop 1
for number in [0, 1, 2, 3, 4]:
    print(number)
print("-" * 30)
# Do the same in a different way
for number in range(5):
    print(number)
print("-" * 30)
for number in range(10, 4, -1):
    print(number)
print("-" * 30)

# More spicy
surnames = ["Rivest", "Shamir", "Adleman"]

for position in range(len(surnames)):
    print(position, surnames[position])
print()

for position in range(len(surnames)):
    print(surnames[position][0], end="")
print()

# Do the same using enumeration
for position, surname in enumerate(surnames):
    print(position, surname)
print()

# Make it start from 1
for position, surname in enumerate(surnames, 1):
    print(position, surname)
