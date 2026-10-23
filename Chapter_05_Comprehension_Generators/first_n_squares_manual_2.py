def get_squares_gen(n):
    for i in range(n):
        yield i**2

def main():
    squares = get_squares_gen(3)
    print(squares)

    try:
        while True:
            print(squares.__next__())

    except StopIteration:
        print("Generator exhausted!")

if __name__ == '__main__':
    main()