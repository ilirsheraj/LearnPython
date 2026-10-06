from math import sqrt, ceil

def get_primes(n):
    """
    Calculates a list of primes up to (and including) n

    Input: integer n
    Returns: a list of primes up to and including n
    """
    primelist = []
    for candidate in range(2, n+1):
        is_prime = True
        root = ceil(sqrt(candidate))
        for prime in primelist:
            if prime > root:
                break
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primelist.append(candidate)
    return primelist

def main():
    num = int(
        input("Please enter a number to find primes until that position: "))
    print(get_primes(num))

if __name__ == '__main__':
    main()
