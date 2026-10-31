class A:
    def __init__(self, factor):
        self.factor = factor

    def op1(self):
        print("OP1 with factor {} ...".format(self.factor))

class B(A):
    def op2(self, factor):
        self.factor = factor
        print("OP2 with factor {} ...".format(self.factor))

def main():
    obj = B(100)
    # print(obj.op2())
    try:
        print(obj.op2())
    except TypeError:
        print("No argument given")

if __name__ == "__main__":
    main()