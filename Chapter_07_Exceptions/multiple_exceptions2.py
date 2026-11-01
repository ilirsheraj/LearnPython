def my_division(values):
    try:
        q, r = divmod(*values)

    except ZeroDivisionError:
        print("You tried to divide by zero")

    except TypeError as e:
        print(e)
    else:
        return (q, r)

def main():
    print(my_division((1,2)))
    print()
    print(my_division((1,0)))
    print()
    print(my_division(("one",2)))

if __name__ == "__main__":
    main()