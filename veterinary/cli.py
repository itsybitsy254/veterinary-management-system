import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, Client, Veterinarian, Specialization, Animal, Appointment, Prescription

DATABASE_URL = "sqlite:///veterinary.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    """CLI for managing veterinary database."""
    pass

@cli.command()
def add_client():
    """Add a new client."""
    name = click.prompt("Enter client's name")
    email = click.prompt("Enter client's email")
    phone = click.prompt("Enter client's phone number")

    client = Client(name=name, email=email, phone=phone)
    session.add(client)
    session.commit()
    click.echo(f"Client '{name}' added.")

@cli.command()
def add_specialization():
    """Add a new specialization."""
    name = click.prompt("Enter specialization name")

    specialization = Specialization(name=name)
    session.add(specialization)
    session.commit()
    click.echo(f"Specialization '{name}' added.")

@cli.command()
def add_veterinarian():
    """Add a new veterinarian and optionally add specializations."""
    name = click.prompt("Enter veterinarian's name")
    
    # List all specializations for reference
    specializations = session.query(Specialization).all()
    if specializations:
        click.echo("Available Specializations:")
        for spec in specializations:
            click.echo(f"ID: {spec.id}, Name: {spec.name}")
    else:
        click.echo("No specializations available.")
    
    specializations_input = click.prompt("Enter specialization IDs (comma-separated)", default='')

    veterinarian = Veterinarian(name=name)
    session.add(veterinarian)

    if specializations_input:
        spec_ids = [int(id) for id in specializations_input.split(',')]
        for spec_id in spec_ids:
            specialization = session.query(Specialization).get(spec_id)
            if specialization:
                veterinarian.specializations.append(specialization)
            else:
                click.echo(f"Specialization ID '{spec_id}' not found.")
    session.commit()
    click.echo(f"Veterinarian '{name}' added.")

@cli.command()
def add_animal():
    """Add a new animal."""
    name = click.prompt("Enter animal's name")
    species = click.prompt("Enter animal's species")
    
    # List all clients for reference
    clients = session.query(Client).all()
    if clients:
        click.echo("Available Clients (Owners):")
        for client in clients:
            click.echo(f"ID: {client.id}, Name: {client.name}, Email: {client.email}")
    else:
        click.echo("No clients available.")
    
    owner_id = click.prompt("Enter owner ID", type=int)
    breed = click.prompt("Enter animal's breed", default='')
    age = click.prompt("Enter animal's age", default=0, type=int)

    owner = session.query(Client).get(owner_id)
    if not owner:
        click.echo(f"Owner ID '{owner_id}' not found.")
        return

    animal = Animal(name=name, species=species, breed=breed, age=age, owner_id=owner_id)
    session.add(animal)
    session.commit()
    click.echo(f"Animal '{name}' added.")

@cli.command()
def add_appointment():
    """Add a new appointment."""
    from datetime import datetime

    date_str = click.prompt("Enter appointment date (YYYY-MM-DD)")
    date = datetime.strptime(date_str, '%Y-%m-%d').date()
    reason = click.prompt("Enter reason for appointment")
    
    # List all clients for reference
    clients = session.query(Client).all()
    if clients:
        click.echo("Available Clients:")
        for client in clients:
            click.echo(f"ID: {client.id}, Name: {client.name}")
    client_id = click.prompt("Enter client ID", type=int)

    # List all animals for reference
    animals = session.query(Animal).all()
    if animals:
        click.echo("Available Animals:")
        for animal in animals:
            click.echo(f"ID: {animal.id}, Name: {animal.name}, Species: {animal.species}")
    animal_id = click.prompt("Enter animal ID", type=int)

    # List all veterinarians for reference
    veterinarians = session.query(Veterinarian).all()
    if veterinarians:
        click.echo("Available Veterinarians:")
        for vet in veterinarians:
            click.echo(f"ID: {vet.id}, Name: {vet.name}")
    veterinarian_id = click.prompt("Enter veterinarian ID", type=int)

    client = session.query(Client).get(client_id)
    animal = session.query(Animal).get(animal_id)
    veterinarian = session.query(Veterinarian).get(veterinarian_id)

    if not client:
        click.echo(f"Client ID '{client_id}' not found. Please add the client first.")
        return
    if not animal:
        click.echo(f"Animal ID '{animal_id}' not found. Please add the animal first.")
        return
    if not veterinarian:
        click.echo(f"Veterinarian ID '{veterinarian_id}' not found. Please add the veterinarian first.")
        return

    appointment = Appointment(date=date, reason=reason, client_id=client_id, animal_id=animal_id, veterinarian_id=veterinarian_id)
    session.add(appointment)
    session.commit()
    click.echo(f"Appointment on {date} added.")

@cli.command()
def add_prescription():
    """Add a new prescription."""
    medication = click.prompt("Enter medication name")
    dosage = click.prompt("Enter dosage")
    
    # List all animals for reference
    animals = session.query(Animal).all()
    if animals:
        click.echo("Available Animals:")
        for animal in animals:
            click.echo(f"ID: {animal.id}, Name: {animal.name}, Species: {animal.species}")
    animal_id = click.prompt("Enter animal ID", type=int)

    animal = session.query(Animal).get(animal_id)
    if not animal:
        click.echo(f"Animal ID '{animal_id}' not found. Please add the animal first.")
        return

    prescription = Prescription(medication=medication, dosage=dosage, animal_id=animal_id)
    session.add(prescription)
    session.commit()
    click.echo(f"Prescription for animal ID '{animal_id}' added.")

@cli.command()
def list_clients():
    """List all clients."""
    clients = session.query(Client).all()
    for client in clients:
        click.echo(f"ID: {client.id}, Name: {client.name}, Email: {client.email}, Phone: {client.phone}")

@cli.command()
def list_veterinarians():
    """List all veterinarians."""
    veterinarians = session.query(Veterinarian).all()
    for vet in veterinarians:
        click.echo(f"ID: {vet.id}, Name: {vet.name}")

@cli.command()
def list_specializations():
    """List all specializations."""
    specializations = session.query(Specialization).all()
    for spec in specializations:
        click.echo(f"ID: {spec.id}, Name: {spec.name}")

@cli.command()
def list_animals():
    """List all animals."""
    animals = session.query(Animal).all()
    for animal in animals:
        click.echo(f"ID: {animal.id}, Name: {animal.name}, Species: {animal.species}, Breed: {animal.breed}, Age: {animal.age}")

@cli.command()
def list_appointments():
    """List all appointments with client, veterinarian, and animal names."""
    appointments = session.query(Appointment).all()
    
    for appointment in appointments:
        client = session.query(Client).get(appointment.client_id)
        animal = session.query(Animal).get(appointment.animal_id)
        veterinarian = session.query(Veterinarian).get(appointment.veterinarian_id)

        click.echo(
            f"ID: {appointment.id}, "
            f"Date: {appointment.date}, "
            f"Reason: {appointment.reason}, "
            f"Client: {client.name if client else 'Unknown'}, "
            f"Animal: {animal.name if animal else 'Unknown'}, "
            f"Veterinarian: {veterinarian.name if veterinarian else 'Unknown'}"
        )

@cli.command()
def list_prescriptions():
    """List all prescriptions with animal names."""
    prescriptions = session.query(Prescription).all()
    
    for prescription in prescriptions:
        animal = session.query(Animal).get(prescription.animal_id)
        
        click.echo(
            f"ID: {prescription.id}, "
            f"Medication: {prescription.medication}, "
            f"Dosage: {prescription.dosage}, "
            f"Animal: {animal.name if animal else 'Unknown'}"
        )

if __name__ == '__main__':
    cli()
