# Parentheses in class are redundant
class Person:
    # Add attribute
    species = "Human"

def main():
    print(Person.species)
    print()
    # Add dynamically: Class Attributes
    Person.alive = True
    print(Person.alive)
    print()
    # New instance
    man = Person()
    print(man.species)
    print(man.alive)
    print()

    # Look at inheritance
    Person.alive = False
    print(man.alive)
    print()

    # Add instance attributes
    man.name = "Darth"
    man.surname = "Vader"
    print(man.name, man.surname)

if __name__ == '__main__':
    main()