# Two ways to raise an error if the loop doesn't find what we were looking for
# First is the classical way, and second with a for-else loop

class DriverException(Exception):
    pass

people = [("James", 17), ("Kirk", 9), ("Lars", 8), ("Robert", 13)]
driver = None

for person, age in people:
    # print(person, age)
    if age >= 18:
        driver = (person, age)
        break

if driver is None:
    raise DriverException("Driver not Found")
