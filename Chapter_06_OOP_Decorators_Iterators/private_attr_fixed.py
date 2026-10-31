class A:
    def __init__(self, factor):
        # name mangling mechanism
        self.__factor = factor

    def op1(self):
        print("Op1 with factor {}...".format(self.__factor))

class B(A):
    def op2(self, factor):
        # name mangling mechanism
        self.__factor = factor
        print("Op2 with factor {}...".format(self.__factor))

def main():
    obj = B(100)
    obj.op1()

    obj.op2(50)
    obj.op1()

    print(obj.__dict__.keys())

if __name__ == "__main__":
    main()