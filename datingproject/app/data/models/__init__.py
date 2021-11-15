from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.data.db import Base


class Person(Base):
    __tablename__ = 'Persons'

    persons_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    birthday = Column(Date, nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(45), nullable=False)
    phone_number = Column(String(45), nullable=False)
    street_address = Column(String(120), nullable=False)
    zipcode = Column(String(15), nullable=False)
    city = Column(String(150), nullable=False)
    country = Column(String(45), nullable=False)
    have_children = Column(Boolean)
    Genders_GenderID = Column(Integer, ForeignKey('Genders.Genderid'))
    Gender = relationship('Gender')


class Gender(Base):
    __tablename__ = 'Genders'

    GenderID = Column(Integer, primary_key=True, autoincrement=True)
    gender_name = Column(String(25), nullable=False)
