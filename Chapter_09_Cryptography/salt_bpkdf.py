import hashlib
import os

# 16 byte random salt
dk = hashlib.pbkdf2_hmac("sha256", b"password123",
                         salt=os.urandom(16), iterations=100000)

print(dk.hex())