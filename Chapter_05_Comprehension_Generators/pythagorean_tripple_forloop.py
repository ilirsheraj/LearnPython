from functions import gcd

def gen_tripple(N):
    for m in range(1, int(N ** 0.5) + 1):
        for n in range(1, m):
            if (m - n) % 2 and gcd(m, n) == 1:
                c = m**2 + n**2
                if c <= N:
                    a = m**2 - n**2
                    b = 2 * m * n
                    yield (a, b, c)

def main():
    print(sorted(gen_tripple(50), key=sum))

if __name__ == "__main__":
    main()