import secrets

# Choose randomly any word from the sentence
print(secrets.choice("Te dua ste dua, mos e tall me mua".split()))
print()
# Pick any number from 0 to the number provided here
print(secrets.randbelow(10**6))
print()
# Generate an integer with random bits specified
print(secrets.randbits(32))