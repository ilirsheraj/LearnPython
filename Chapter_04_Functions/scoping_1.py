# define test in the global scope
test = 0

def my_function():
    # Define test in the local scope
    test = 1
    print("my_function: ", test)

def main():
    my_function()
    print("global: ", test)

if __name__ == "__main__":
    main()

