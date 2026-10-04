def func(a, b, c=7, *args, **kwargs):
    print("a, b, c:", a, b, c)
    print("args:", args)
    print("kwargs:", kwargs)

def main():
    func(1,2,3,4,5,7,A="a", B="b")

if __name__ == "__main__":
    main()