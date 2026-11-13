import secrets

# A random byte string as specified
print(secrets.token_urlsafe(32))
print()
# Tokens in hexadecimal format
print(secrets.token_hex(32))
print()
# URL-Like tokens
print(secrets.token_urlsafe(32))