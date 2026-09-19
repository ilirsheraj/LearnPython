# Now use the walrus operator
flavors = ["pistachio", "malaga", "vanilla", "chocolate", "strawberry"]

prompt = "Choose your favorite flavor: "
print(flavors)

while (choice := input(prompt)) not in flavors:
    print(f"Sorry, '{choice}' is not an available option")
    print(f"Please choose one of these options: {flavors}")
print(f"You chose '{choice}'")
