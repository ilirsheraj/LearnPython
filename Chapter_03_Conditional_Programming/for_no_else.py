class DriverException(Exception):
    pass

people = [("James", 17), ("Kirk", 9), ("Lars", 8), ("Robert", 13)]
driver = None

for person, age in people:
    if age >= 18:
        driver = (person, age)
        break

else:
    raise DriverException("Driver not Found!")