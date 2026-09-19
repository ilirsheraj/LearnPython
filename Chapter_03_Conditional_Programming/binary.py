# Calculate the binary representation of some number
print("Calculate the binary representation of 39\n")

n = 39
reminders = []

while n > 0:
    reminder = n % 2
    reminders.append(reminder)
    n //= 2

# We need to take the reverse of reminders to calculate the binary representation
reminders.reverse()
# print(reminders)
print(f'The binary representation of 39 is : {"".join(map(str, reminders))}')

# Use the divmod() function
n = 39
remainders = []

while n > 0:
    n, remainder = divmod(n, 2)
    remainders.append(remainder)

remainders.reverse()
# print(remainders)
print("".join(map(str, reminders)))