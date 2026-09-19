def primes(up_to: int) -> list[int]:
    primes = []
    for i in range(2, up_to + 1):
        is_prime = True
        for div in range(2, i):
            if i % div == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

def main():
    primes_100 = primes(100)
    print(primes_100)

if __name__ == '__main__':
    main()