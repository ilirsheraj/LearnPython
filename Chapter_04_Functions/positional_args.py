# Define a function with Variable Positional Parameter
def minimum(*n):
    # Print the type of n; it must be tuple
    # print(type(n))
    # Collective objects evaluate to false when empty and true otherwise
    if n:
        mn = n[0]
        for value in n[1:]:
            if value < mn:
                mn = value
        print(mn)

    else:
        print("You provided no arguments!")

def main():
    minimum(1, 3, -7, 9)
    print()
    minimum()

if __name__ == '__main__':
    main()

