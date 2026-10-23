# Define a classical function
def get_squares(n):
    return [i **2 for i in range(n)]

# Define a generator function
def get_squares_gen(n):
    for x in range(n):
        yield x**2

def main():
    print(get_squares(10))
    print()
    print(list(get_squares_gen(10)))

if __name__ == '__main__':
    main()