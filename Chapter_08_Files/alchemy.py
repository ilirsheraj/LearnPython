from alchemy_models import Person, Address, engine
from sqlalchemy.orm import sessionmaker

# First create the session
Session = sessionmaker(bind=engine)
session = Session()

# Create two people
anakin = Person(name="Anakin Skywalker", age=32)
obi1 = Person(name="Obi-wan", age=40)

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