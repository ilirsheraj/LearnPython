# Let's make it a bit more spicy
# define the global scope
test = 0
def outer():
    # Define the outer scope
    test = 1

    def inner():
        # define the inner scope
        test = 2
        print("inner:", test)
    # call the inner function: expected 2
    inner()
    # outer function expects 1
    print("outer: ", test)

def main():
    # expect 2 then 1
    outer()
    # then finally global
    print("global: ", test)

if __name__ == "__main__":
    main()