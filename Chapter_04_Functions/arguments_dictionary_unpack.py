def func(a, b, c):
    print(a, b, c)

def main():
    values = dict(zip(["b", "c", "a"], [1, 2, 42]))
    print(values)
    func(**values)

if __name__ == '__main__':
    main()