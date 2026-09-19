# Write a function to capture prime numbers up to a certain point
primes = []
upto = 100

for n in range(2, upto + 1):
    # print(n)
    is_prime = True
    # This will not run for range (2,2), so 2 gone by default
    for divisor in range(2, n):
        if n % divisor == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(n)
print(primes)
