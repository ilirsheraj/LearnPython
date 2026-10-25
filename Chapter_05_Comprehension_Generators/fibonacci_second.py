def fibonacci(n):
    """Returns all Fibonacci numbers up to n."""
    yield 0
    if n == 0:
        return
    a, b = 0, 1
    while b <= n:
        yield b
        a, b = b, a + b

def main():
    print(list(fibonacci(0)))
    print(list(fibonacci(1)))
    print(list(fibonacci(50)))

if __name__ == '__main__':
    main()