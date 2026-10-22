from string import ascii_lowercase

# ascii_lowercase = ascii_lowercase
# print(ascii_lowercase)
# Creates a letter-index pair dictionary
letter_map = {c: k for k, c in enumerate(ascii_lowercase)}
print(letter_map)