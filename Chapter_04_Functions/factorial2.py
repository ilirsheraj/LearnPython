# Let's use a bunch of built-in packages
from functools import reduce
from operator import mul

def factorial(n):
    return reduce(mul, range(1, n+1))

def main():
    f5 = factorial(5)
    print(f5)

if __name__ == '__main__':
    main()