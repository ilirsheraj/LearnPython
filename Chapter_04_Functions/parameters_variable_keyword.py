def func(**kwargs):
    print(kwargs)

def main():
    func(a=1, b=42)
    func()
    func(a=1, b=46, c=99)

if __name__ == '__main__':
    main()