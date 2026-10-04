def moddiv(a, b):
    return a//b, a % b

def main():
    a, b = moddiv(20, 7)
    print(a, b)

if __name__ == '__main__':
    main()