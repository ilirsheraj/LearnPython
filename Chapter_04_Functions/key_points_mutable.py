x = [1, 2, 3]

def func(x):
    x[1] = 42
    print(id(x))

def main():
    print(id(x))
    func(x)
    print(x)
    print(id(x))

if __name__ == '__main__':
    main()