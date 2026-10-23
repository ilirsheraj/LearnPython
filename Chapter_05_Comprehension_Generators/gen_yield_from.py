# Using yield from
def print_squares(start, end):
    yield from (n**2 for n in range(start, end))

def main():
    for n in print_squares(2, 10):
        print(n)

if __name__ == '__main__':
    main()