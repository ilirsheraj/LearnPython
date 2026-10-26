from time import time, sleep

def f(sleeping_time=0.1):
    sleep(sleeping_time)

def measure(func):
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)

        print(func.__name__, time() - t)
    return wrapper


# decoration point
f = measure(f)
f(0.2)
print()
f(sleeping_time=0.3)
print()
print(f.__name__)
