# Example to follow MRO (Method Resolution Order)
class A:
    label = "a"

class B(A):
    pass

class C(A):
    label = "c"

class D(B, C):
    pass

def main():
    d = D()
    # Will first inherit from C since B has no attribute
    print(d.label)
    print(d.__class__.__mro__)

if __name__ == "__main__":
    main()