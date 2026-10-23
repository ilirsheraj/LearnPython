def counter(start=0):
    """
    This function will run forever
    use next and it will go on, or use list and it will 
    go on non-stop until you kill it
    """
    n = start
    while True:
        yield n
        n += 1

def main():
    c = counter()
    # This will start from 3 where print above left
    for i in range(10):
        print(next(c))

if __name__ == '__main__':
    main()