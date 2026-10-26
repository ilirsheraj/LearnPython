from time import sleep, time
# Define function for delay

def f():
    sleep(0.3)

def g():
    sleep(0.5)

def main():
    t = time()
    f()
    print(f"f took {time() - t} seconds")
    print()
    t = time()
    g()
    print(f"g took {time() - t} seconds")

if __name__ == '__main__':
    main()