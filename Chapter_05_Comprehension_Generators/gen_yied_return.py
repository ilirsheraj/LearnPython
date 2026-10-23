# define a geometric function
def geometric_progression(a, q):
    """
    Define a geometric progression function
    it returns aq**0, aq**1, aq**2, aq**3 ... aq**k
    """
    k = 0
    while True:
        result = a * q ** k
        if result <= 100_000:
            yield result
        else:
            # return statement causes a StopIteration exception
            return
        k += 1


def main():
    for n in geometric_progression(2, 5):
        print(n)

if __name__ == '__main__':
    main()