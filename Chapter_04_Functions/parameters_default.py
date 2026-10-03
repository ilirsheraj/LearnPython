def func(a, b=4, c=88):
    print(a, b, c)

def main():
    func(1)
    print()
    func(b=5, a=7, c=9)
    print()
    func(42, c=9)
    func(42, 43, 44)

if __name__ == '__main__':
    main()