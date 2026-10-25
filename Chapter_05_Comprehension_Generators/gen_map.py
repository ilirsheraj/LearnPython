def adder(*n):
    return sum(n)

def main():
    # adds (0,1), (1,2) ... (99, 100) -> 1, 3, 5, ... 199
    s1 = sum(map(adder, range(100), range(1, 101)))
    print(s1)

    s2 = sum(adder(*n) for n in zip(range(100), range(1, 101)))
    print(s2)

if __name__ == '__main__':
    main()