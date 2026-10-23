def counter(start=0):
    n = start
    while True:
        result = yield n
        print(type(result), result)

        if result == 'Q':
            break
        n+=1

def main():
    try:
        c = counter()
        print(next(c))
        print(c.send("Wow!"))
        print(next(c))
        print(c.send("Q"))
    except StopIteration:
        print("Generator Stopped!")

if __name__ == '__main__':
    main()