import timeit

def square1(n):
    # Square through the power operator
    return n ** 2

def square2(n):
    # Square through multiplication
    return n * n

def main():
    # Run the function 1M times and check their differences
    time1 = timeit.timeit(lambda: square1(10), number=1_000_000)
    time2 = timeit.timeit(lambda: square2(10), number=1_000_000)

    print(f"square1 (n ** 2): {time1:.6f} seconds")
    print(f"square2 (n * n):  {time2:.6f} seconds")

    print(f"\nDifference: {abs(time1 - time2):.6f} seconds")
    print(f"Speed ratio: {max(time1, time2) / min(time1, time2):.2f}x")

if __name__ == '__main__':
    main()