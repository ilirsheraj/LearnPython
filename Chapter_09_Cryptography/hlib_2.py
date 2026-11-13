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
print(h.digest_size)
print(h.name)
print()

# Do the same using sha256 (we use this in genomics a lot)
print(hashlib.sha256(b'Hash me now!').hexdigest())