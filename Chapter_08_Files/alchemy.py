from alchemy_models import Person, Address, engine
from sqlalchemy.orm import sessionmaker

# First create the session
Session = sessionmaker(bind=engine)
session = Session()

# Create two people
anakin = Person(name="Anakin Skywalker", age=32)
obi1 = Person(name="Obi-Wan Kenobi", age=40)

# Add e-mail addresses: two ways
obi1.addresses = [
    Address(email="obi1@example.com"),
    Address(email="wanwan@example.com"),
]

anakin.addresses.append(Address(email="ani@example.com"))
anakin.addresses.append(Address(email="evil.dart@example.com"))
anakin.addresses.append(Address(email="vader@example.com"))

# Now database time
session.add(anakin)
session.add(obi1)
# To save the data into the database
session.commit()

obi1 = session.query(Person).filter(
    # start with Obi: like()
    Person.name.like("Obi1%")
).first()
print(anakin, anakin.addresses)
print()

# Capture Anankin id
anakin_id = anakin.id
# remove it
del anakin

def display_info():
    # Get all addresses first
    addresses = session.query(Address).all()

    # Display results
    for address in addresses:
        print(f"{address.person.name}: <{address.email}>")

    print("people: {}, addresses: {}".format(
        session.query(Person).count(),
        session.query(Address).count(),
    ))

display_info()
print()
# Get anankin by ID
anakin = session.query(Person).get(anakin_id)
# Delete it
session.delete(anakin)
session.commit()

# Display one more to see the changes
display_info()