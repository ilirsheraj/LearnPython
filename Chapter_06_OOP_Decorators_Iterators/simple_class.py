class Simplest():
    pass

def main():
    print(type(Simplest))
    simp = Simplest()
    print(type(simp))
    print(type(simp) is Simplest)

if __name__ == '__main__':
    main()