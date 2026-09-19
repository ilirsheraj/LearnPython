# More efficient way of generating prime numbers
primes = []
upto = 100

for n in range(2, upto + 1):
    # 2 will go automatically because of range(2,2)
    for divisor in range(2, n):
        if n % divisor == 0:
            break
    else:
        primes.append(n)

print(primes)
