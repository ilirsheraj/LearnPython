# Use while loop for iterables (too long and boring)
people = ["Nick", "Rick", "Roger", "Syd"]
ages = [23, 24, 23, 21]
position = 0
while position < len(people):
    person = people[position]
    age = ages[position]
    print(person, age)
    position += 1
print()
# Make it a bit shorter
idx = 0
while idx < len(people):
    print(people[idx], ages[idx])
    idx += 1

