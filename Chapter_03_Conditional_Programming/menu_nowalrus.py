# Choice of menu in conventional way
flavors = ["pistachio", "malaga", "vanilla", "chocolate", "strawberry"]

prompt = "Choose your favorite flavor: "
print(flavors)

while True:
    choice = input(prompt)

    if choice in flavors:
        break
    print(f"Sorry, '{choice}' is not an available option")
    print(f"Please chose of the these options {flavors}")
print(f"You chose '{choice}'")
