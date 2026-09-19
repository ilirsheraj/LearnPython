people = ["Nick", "Rick", "Roger", "Syd"]
ages = [23, 24, 23, 21]

print("Classical for-loop:\n")

for position in range(len(people)):
    person = people[position]
    age = ages[position]
    print(person, age)

print()
print("-" * 20)
print("Use Enumerate:\n")

for position, person in enumerate(people):
    age = ages[position]
    print(person, age)

print()
print("-" * 20)
print("Use zip:\n ")

for person, age in zip(people, ages):
    print(person, age)

print()
print("-" * 20)

instruments = ["Drums", "Keyboards", "Bass", "Guitar"]
for person, age, instrument in zip(people, ages, instruments):
    print(person, age, instrument)

print()
print("-" * 20)

for data in zip(people, ages, instruments):
    person, age, instrument = data
    print(f"Tuple form: {data}")
    print(person, age, instrument)