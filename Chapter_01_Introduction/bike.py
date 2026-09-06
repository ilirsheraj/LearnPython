#bike.py
# define a simple class for bikes

class Bike:

    # Body of the class
    # Initializer Method: starts with "magic method"
    def __init__(self, colour, frame_material):
        self.colour = colour
        self.frame_material = frame_material
        
    def brake(self):
        print("Braking!")
        
# Create two class instances: red bike and a blue bike
red_bike = Bike("Red", "Carbon Fiber")
blue_bike = Bike("Blue", "Steel")

# Now we can inspect the instances we created
print(red_bike.colour)
print(red_bike.frame_material)
print(blue_bike.colour)
print(blue_bike.frame_material)

red_bike.brake()
