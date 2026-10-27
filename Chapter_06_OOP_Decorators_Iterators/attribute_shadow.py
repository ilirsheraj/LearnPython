class Point:
    # Define two attributes for the class
    x = 10
    y = 7

def main():
    p = Point()
    # This inherits the attributes of class
    print(p.x)
    print(p.y)
    print()

    # Now we give p its own attribute
    p.x = 12
    print(p.x)
    # Class attribute remains unchanged
    print(Point.x)
    print()

    # Now lets delete x attribute of p
    del p.x
    # class attribute kicks in
    print(p.x)

    # Define a new attribute for p instance
    p.z = 3
    print(p.z)
    print()

    # Check that this attribute does not exist for the main class
    try:
        print(Point.z)
    except AttributeError:
        print("This attribute is not found on the main class")

if __name__ == '__main__':
    main()