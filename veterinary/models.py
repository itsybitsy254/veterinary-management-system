from sqlalchemy import Column, Integer, String, ForeignKey, Table, Date, Text
from sqlalchemy.orm import relationship
from veterinary.db import Base

# Association Table between Veterinarian and Specialization
veterinarian_specialization = Table(
    'veterinarian_specialization', Base.metadata,
    Column('veterinarian_id', Integer, ForeignKey('veterinarians.id'), primary_key=True),
    Column('specialization_id', Integer, ForeignKey('specializations.id'), primary_key=True)
)

class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=False, unique=True)
    animals = relationship("Animal", back_populates="owner")
    appointments = relationship("Appointment", back_populates="client")

class Animal(Base):
    __tablename__ = 'animals'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)
    breed = Column(String)
    age = Column(Integer)
    owner_id = Column(Integer, ForeignKey('clients.id'))
    owner = relationship("Client", back_populates="animals")
    prescriptions = relationship("Prescription", back_populates="animal")
    appointments = relationship("Appointment", back_populates="animal")

class Veterinarian(Base):
    __tablename__ = 'veterinarians'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    specializations = relationship('Specialization', secondary=veterinarian_specialization, back_populates='veterinarians')
    appointments = relationship("Appointment", back_populates="veterinarian")

class Specialization(Base):
    __tablename__ = 'specializations'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    veterinarians = relationship('Veterinarian', secondary=veterinarian_specialization, back_populates='specializations')

class Appointment(Base):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    reason = Column(Text, nullable=False)
    client_id = Column(Integer, ForeignKey('clients.id'))
    client = relationship("Client", back_populates="appointments")
    animal_id = Column(Integer, ForeignKey('animals.id'))
    animal = relationship("Animal", back_populates="appointments")
    veterinarian_id = Column(Integer, ForeignKey('veterinarians.id'))
    veterinarian = relationship("Veterinarian", back_populates="appointments")

class Prescription(Base):
    __tablename__ = 'prescriptions'
    id = Column(Integer, primary_key=True)
    medication = Column(String, nullable=False)
    dosage = Column(String, nullable=False)
    animal_id = Column(Integer, ForeignKey('animals.id'))
    animal = relationship("Animal", back_populates="prescriptions")
