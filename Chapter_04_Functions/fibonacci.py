def fibonacci(n):
    """
    The function returns the fibonacci number of n
    """
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

def main():
    num = int(input("Please insert a number to calculate its Fibonacci: "))
    print(fibonacci(num))

if __name__ == "__main__":
    main()