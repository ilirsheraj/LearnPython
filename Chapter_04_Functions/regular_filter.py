def is_multiple_of_five(n):
    """
    The function tests if a number is multiple of 5
    If it is, the number is returned, otherwise it is not returned
    """
    return not n % 5

def get_multiples_of_five(n):
    return list(filter(is_multiple_of_five, range(n+1)))

def main():
    num = int(input("Please enter a number: "))
    print(get_multiples_of_five(num))

if __name__ == "__main__":
    main()