# Not Frequent
def kwo(*a, c):
    print(a, c)

def kwo2(a, b=42, *, c):
    print(a, b, c)

def main():
    kwo(1, 2, 3, c=7)
    kwo(c=4)
    # kwo(1, 2) # Gives error, c not defined

    kwo2(3, b=7, c=99)
    kwo2(3, c = 13)
    #kwo2(3, 23) # gives error, c not defined

if __name__ == '__main__':
    main()
