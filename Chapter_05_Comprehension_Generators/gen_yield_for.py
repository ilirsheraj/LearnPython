# The classical Approach
def print_squares(start, end):
    for n in range(start, end):
        yield n**2

def main():
    for n in print_squares(2,10):
        print(n)

if __name__ == '__main__':
    main()