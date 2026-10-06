def get_multiples_of_five(n):

    return list(filter(lambda x: not x % 5, range(n+1)))

def main():
    num = int(input("Please enter a number: "))
    print(get_multiples_of_five(num))

if __name__ == "__main__":
    main()