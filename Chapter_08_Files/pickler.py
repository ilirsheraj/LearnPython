import pickle
from dataclasses import dataclass

@dataclass
class Person:
    first_name: str
    last_name: str
    id: int

    def greet(self):
        print(f"Hello, I am {self.first_name} {self.last_name}"
              f" and my ID is {self.id}")

people = [
    Person("John", "Doe", 123),
    Person("Anakyn", "Skywalker", 456),
]

# Save data in binary format
with open("data.pickle", "wb") as stream:
    pickle.dump(people, stream)

# Load data back from file
with open("data.pickle", "rb") as stream:
    peeps = pickle.load(stream)

# call all
for person in peeps:
    person.greet()