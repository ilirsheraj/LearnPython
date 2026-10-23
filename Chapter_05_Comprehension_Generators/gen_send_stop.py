# First define stop as False
stop = False
def counter(start=0):
    """
    Again we will call the geenrator as long as stop is True
    Define stop = False outside and it will stop
    """
    n = start
    while not stop:
        yield n
        n += 1

def main():
    # If you want to use while loop
    global stop
    i = 0
    c = counter()

    # Now use the while loop (to avoid crashing use try-except)
    while True:
        try:
            print(next(c))
            i += 1
            if i > 10:
                stop = True

        except StopIteration:
            print("Generator exhausted!")
            break

if __name__ == '__main__':
    main()