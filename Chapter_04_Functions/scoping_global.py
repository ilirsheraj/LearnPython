# Define the same function now using global scope
test = 0   # real global
def outer():
    # define outer scope
    test = 1

    # define inner function
    def inner():
        # define global scope
        global test
        test = 2
        print("inner:", test)

    inner()
    print("outer:", test)

def main():
    outer()
    print("global:", test)

if __name__ == "__main__":
    main()
