# Let's see a case of multiple inheritance
# Define a base class
class Shape:
    geometric_type = "Generic Shape"
    def area(self):
        # This acts as a placeholder for the inheritance
        raise NotImplementedError

    def get_geometric_type(self):
        return self.geometric_type

# Another base Class
class Plotter:
    def plot(self, ratio, topleft):
        # BS here, just for the sake of definition
        print("Plotting at {}, ratio {}.".format(
            topleft, ratio))

# Polygon Baseclass (Inherits from both Shape and Plotter)
class Polygon(Shape, Plotter):
    # This is the base class for the polygons
    geometric_type = "Polygon"

class RegularPolygon(Polygon):
    # Is-A Polygon
    geometric_type = "Regular Polygon"
    # Since regular polygon has equal sides and angles, lets define side
    def __init__(self, side):
        self.side = side

class RegularHexagon(RegularPolygon):
    # Is-A RegularPolygon
    geometric_type = "Regular Hexagon"
    def area(self):
        return 1.5 * (3 ** 0.5 * self.side **2)

class Square(RegularPolygon):
    # Is-A RegularPolygon
    geometric_type = "Square"
    def area(self):
        return self.side * self.side

def main():
    # Instantiate a hexagon with side 10
    hexagon = RegularHexagon(10)
    print(f"The area of hexagon is {hexagon.area():.2f}")
    print(f"The geometric shape of hexagon is {hexagon.get_geometric_type()}")
    hexagon.plot(0.8, (75, 77))
    print()

    # Instantiate a Square with side 12
    square = Square(12)
    print(f"The area of the square is {square.area():.2f}")
    print(f"The shape of the square is {square.get_geometric_type()}")
    square.plot(0.93, (74, 75))

if __name__ == "__main__":
    main()