def func(a, b, c):
    print(a, b, c)

def main():
    values = (1, 3, -7)
    func(*values)

if __name__ == '__main__':
    main()