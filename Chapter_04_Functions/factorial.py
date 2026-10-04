def factorial(n):
    """
    A function that calculates the factorial of n-numbers
    """
    if n in (0, 1):
        return 1
    # Assign the largest value
    result = n
    for k in range(2, n):
        result *= k
    return result

def main():
    f5 = factorial(5)
    print(f5)

if __name__ == '__main__':
    main()