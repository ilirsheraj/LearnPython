from typing import List, Optional
from sqlalchemy import ForeignKey, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

engine = create_engine("sqlite:///:memory:")

class Base(DeclarativeBase):
    pass

class Person(Base):
    __tablename__ = "person"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]
    age: Mapped[Optional[int]]

    addresses: Mapped[List["Address"]] = relationship(
        back_populates="person",
        order_by="Address.email",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"{self.name}(id={self.id})"

class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[Optional[str]]
    person_id: Mapped[Optional[int]] = mapped_column(ForeignKey("person.id"))

    person: Mapped[Optional["Person"]] = relationship(back_populates="addresses")

Base.metadata.create_all(engine)