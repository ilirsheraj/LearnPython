import hashlib

# use blake2b to hash a message
h = hashlib.blake2b()
# Add the data in two steps rather than one
h.update(b'Hash me')
h.update(b' now!')
print(h.hexdigest())
print()
print(h.digest())
print()
print(h.block_size)
print()
print(h.digest_size)
print()
print(h.name)