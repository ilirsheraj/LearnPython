class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def print_shape(shape):
    print(f"{shape.__class__.__name__} Area: {shape.area()}")

def main():
    circle = Circle(5)
    # print(circle.area())
    rectangle = Rectangle(4, 6)
    # print(rectangle.area())

    print_shape(circle)
    print_shape(rectangle)

if __name__ == "__main__":
    main()