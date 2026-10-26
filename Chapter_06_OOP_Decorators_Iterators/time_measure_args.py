from time import sleep, time

# Let's add arguments to the function
def f(sleep_time = 0.1):
    """Change the time as you like, default is 0.1 seconds"""
    sleep(sleep_time)

def measure(func, *args, **kwargs):
    """
    This is a high-order function that measures the execution time
    It takes another function as argument and returns whatever is
    defined in that function
    """
    t = time()
    func(*args, **kwargs)
    print(func.__name__, "took: ", time() - t)

def add(a, b, verbose=False):
    if verbose:
        print(a + b)

def make_coffee(size="small", sugar=0, milk=False):
    print(f"Making a {size} coffee with {sugar} sugar(s), milk={milk}")
    sleep(0.3)

def main():
    measure(f, sleep_time = 0.3)
    print()
    measure(f, 0.2)
    print()
    measure(f)
    print()
    # use add function with *args
    measure(add, 3, 4, verbose=True)
    # now with kwargs
    measure(make_coffee, size="large", sugar=2, milk=True)

if __name__ == '__main__':
    main()