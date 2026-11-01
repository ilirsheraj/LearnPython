def squareroot(number):
    """Calculate the square root of a number."""
    if number < 0:
        raise ValueError("No negative number please")
    return number ** 0.5

def quadratic(a, b, c):
    """
    Calculate the quadratic equation
    ax^2 + bx + c
    And the Discriminant
    d = b^2 - 4ac
    """
    d = b**2 - 4*a*c

    return ((-b - squareroot(d)) / (2 * a),
            (-b + squareroot(d)) / (2 * a))

def main():
    print(quadratic(1, 2, 1))

    # This will give an error
    print(quadratic(1, 0, 1))

if __name__ == "__main__":
    main()