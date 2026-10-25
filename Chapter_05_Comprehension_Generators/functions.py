def gcd(a, b):
    """
    Calculates the greatest common divisor
    """
    while b != 0:
        a, b = b, a % b
    return a

# print(gcd(13, 3))
# print(gcd(12, 3))
