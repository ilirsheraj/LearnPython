import hashlib

# 16 bytes long hashes
h1 = hashlib.blake2b(b'Important data', digest_size=16,
                     person=b'part-1')
h2 = hashlib.blake2b(b'Important data', digest_size=16,
                     person=b'part-2')
h3 = hashlib.blake2b(b'Important data', digest_size=16)

print(h1.hexdigest())
print()
print(h2.hexdigest())
print()
print(h3.hexdigest())