# Again define a generator function
def get_squares_gen(n):
    for x in range(n):
        yield x ** 2

def main():
    squares = get_squares_gen(4)
    print(squares)
    try:
        while True:
            print(next(squares))
    except StopIteration:
        print("Generator exhausted!")

if __name__ == '__main__':
    main()