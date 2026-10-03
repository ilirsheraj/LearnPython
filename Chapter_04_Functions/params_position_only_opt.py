def func(a, b=2, /):
    print(a, b)

def main():
    func(4, 5)
    print()
    func(1)

if __name__ == '__main__':
    main()