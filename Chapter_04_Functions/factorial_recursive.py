def factorial(n):
    """
    This is a recursive function calculating the factorial of n-numbers
    """
    if n in (0, 1):
        return 1
    return factorial(n-1) * n

def main():
    num = int(input("Please insert a number to calculate its factorial: "))
    print(factorial(num))

if __name__ == '__main__':
    main()