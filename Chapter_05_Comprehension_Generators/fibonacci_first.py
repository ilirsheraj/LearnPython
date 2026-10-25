def fibonacci(N):
    """Returns all Fibonacci numbers up to N."""
    result = [0]
    next_n = 1
    while next_n <= N:
        result.append(next_n)
        next_n = sum(result[-2:])
    return result

def main():
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(50))

if __name__ == '__main__':
    main()