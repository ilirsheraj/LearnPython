def func_name(name, /, **kwargs):
    """
    A mixture of positional-only (left of /) and 
    **kwargs in the same function
    """
    print(name)
    print(kwargs)

def main():
    func_name("Positional-only name", name="Name in Kwargs",
              surname="BS in Surname")

if __name__ == '__main__':
    main()
