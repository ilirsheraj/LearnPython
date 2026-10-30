class Square:
    side = 8
    def area(self):
        return self.side ** 2

def main():
    sq = Square()
    print(sq)
    print()
    print(sq.area)
    # The easy syntax and python takes care of it
    print(sq.area())
    print()
    # The more complete way
    print(Square.area(sq))
    print()

    # Change side and area will change automatically
    sq.side = 10
    print(sq.area())

if __name__ == "__main__":
    main()