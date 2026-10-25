def fibonacci(N):
    """
    Returns all Fibonacci numbers up to N
    """
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b

def main():
    print(list(fibonacci(0)))
    print(list(fibonacci(10)))
    print(list(fibonacci(50)))
if __name__ == '__main__':
    main()