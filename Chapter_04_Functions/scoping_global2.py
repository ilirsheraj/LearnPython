test = 0

def outer():
    test = 1
    print("outer:", test)

def inner():
    global test
    test = 2
    print("inner:", test)

def main():
    inner()
    outer()
    print("global:", test)

if __name__ == "__main__":
    main()
