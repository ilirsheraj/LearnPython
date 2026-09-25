# Define nonlocal scope
def outer():
    # define the outer scope
    test = 1

    # define an inner function
    def inner():
        # define the inner scope: This only works on enclosing scope
        nonlocal test
        test = 2
        print("inner:", test)

    inner()
    print("outer:", test)

def main():
    test = 0
    outer()
    print("global:", test)

if __name__ == "__main__":
    main()





