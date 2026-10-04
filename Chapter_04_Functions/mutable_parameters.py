def func(a=[], b={}):
    print(a)
    print(b)
    print("#" * 12)
    # This will change a
    a.append(len(a))
    # Same thing here, dictionary is mutable
    b[len(a)] = len(a)

def main():
    func()
    func()
    func()
    func()

if __name__ == "__main__":
    main()