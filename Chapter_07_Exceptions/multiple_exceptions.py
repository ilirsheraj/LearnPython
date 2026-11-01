def my_div(values):
    try:
        q, r = divmod(*values)
    except (ZeroDivisionError, TypeError) as e:
        print(e)
    else:
        return (q, r)

def main():
    values = (1, 2)
    print(my_div(values))

    values = (1, 0)
    print(my_div(values))

    values = ("one", 2)
    print(my_div(values))

if __name__ == "__main__":
    main()