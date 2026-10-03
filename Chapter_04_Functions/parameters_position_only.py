def func(a, b, /, c):
    # a and b must be passed positonaly, not by keyword
    print(a, b, c)

def main():
    func(1, 2, c=3)
    print()
    print(1, 2, 3)

    try:
        func(1, b=2, c=3)
    except TypeError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()