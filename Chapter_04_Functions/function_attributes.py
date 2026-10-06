def multiplication(a, b=1):
    return a * b

if __name__ == '__main__':
    special_attributes = [
        "__doc__", "__name__", "__qualname__", "__module__",
        "__defaults__", "__code__", "__globals__", "__dict__",
        "__closure__", "__annotations__", "__kwdefaults__",
    ]

    for attributes in special_attributes:
        print(attributes, "->", getattr(multiplication, attributes))