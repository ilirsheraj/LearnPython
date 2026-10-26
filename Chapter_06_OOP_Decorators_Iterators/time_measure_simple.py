# Define some simple functions to measure time
from time import sleep, time

def f():
    sleep(0.3)

def g():
    sleep(0.5)

def measure(func):
    t = time()
    func()
    print(func.__name__, "took: ", time() - t)

def main():
    measure(f)
    print()
    measure(g)

if __name__ == "__main__":
    main()