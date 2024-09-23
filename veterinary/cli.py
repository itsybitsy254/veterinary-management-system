import click
from sqlalchemy import create_engine
from datetime import datetime
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
def menu():
    """Show a numbered menu of available commands."""
    while True:
        click.echo("\nVeterinary Management System Menu:")
        commands = [
            "Add a new client",
            "Add a new specialization",
            "Add a new veterinarian",
            "Add a new animal",
            "Add a new appointment",
            "Add a new prescription",
            "List all clients",
            "List all veterinarians",
            "List all specializations",
            "List all animals",
            "List all appointments",
            "List all prescriptions",
            "Delete a client",
            "Delete a veterinarian",
            "Delete a specialization",
            "Delete an animal",
            "Delete an appointment",
            "Delete a prescription",
            "Exit"
        ]

        for i, command in enumerate(commands, 1):
            click.echo(f"{i}. {command}")

        choice = click.prompt("Enter the number of the action you want to perform", type=int)

        commands_map = {
            1: "add-client",
            2: "add-specialization",
            3: "add-veterinarian",
            4: "add-animal",
            5: "add-appointment",
            6: "add-prescription",
            7: "list-clients",
            8: "list-veterinarians",
            9: "list-specializations",
            10: "list-animals",
            11: "list-appointments",
            12: "list-prescriptions",
            13: "delete-client",
            14: "delete-veterinarian",
            15: "delete-specialization",
            16: "delete-animal",
            17: "delete-appointment",
            18: "delete-prescription"
        }

        if choice == 19:
            click.echo("Exiting the menu.")
            break

        if choice in commands_map:
            command_name = commands_map[choice]
            click.echo(f"Running: {commands[choice - 1]}")
            cmd = cli.get_command(None, command_name)
            if cmd:
                with click.Context(cmd) as ctx:
                    cmd.invoke(ctx)
        else:
            click.echo("Invalid choice. Please try again.")

# Command implementations
@cli.command('add-client')
def add_client():
    """Add a new client."""
    name = click.prompt("Enter client's name")
    email = click.prompt("Enter client's email")
    phone = click.prompt("Enter client's phone number")
    client = Client(name=name, email=email, phone=phone)
    session.add(client)
    session.commit()
    click.echo(f"Client '{name}' added.")

@cli.command('add-specialization')
def add_specialization():
    """Add a new specialization."""
    name = click.prompt("Enter specialization name")
    specialization = Specialization(name=name)
    session.add(specialization)
    session.commit()
    click.echo(f"Specialization '{name}' added.")

@cli.command('add-veterinarian')
def add_veterinarian():
    """Add a new veterinarian and optionally add specializations."""
    name = click.prompt("Enter veterinarian's name")
    specializations = session.query(Specialization).all()
    
    if specializations:
        click.echo("Available Specializations:")
        for spec in specializations:
            click.echo(f"ID: {spec.id}, Name: {spec.name}")

    specializations_input = click.prompt("Enter specialization IDs (comma-separated)", default='')
    veterinarian = Veterinarian(name=name)
    session.add(veterinarian)

    if specializations_input:
        spec_ids = [int(id.strip()) for id in specializations_input.split(',')]
        for spec_id in spec_ids:
            specialization = session.query(Specialization).get(spec_id)
            if specialization:
                veterinarian.specializations.append(specialization)
            else:
                click.echo(f"Specialization ID '{spec_id}' not found.")
    session.commit()
    click.echo(f"Veterinarian '{name}' added.")

@cli.command('add-animal')
def add_animal():
    """Add a new animal."""
    name = click.prompt("Enter animal's name")
    species = click.prompt("Enter animal's species")
    breed = click.prompt("Enter animal's breed", default="")
    age = click.prompt("Enter animal's age", type=int)

    owners = session.query(Client).all()
    if owners:
        click.echo("Available Clients:")
        for owner in owners:
            click.echo(f"ID: {owner.id}, Name: {owner.name}")
        owner_id = click.prompt("Enter the owner's ID", type=int)
    else:
        click.echo("No clients available.")
        return

    animal = Animal(name=name, species=species, breed=breed, age=age, owner_id=owner_id)
    session.add(animal)
    session.commit()
    click.echo(f"Animal '{name}' added.")

@cli.command('add-appointment')
def add_appointment():
    """Add a new appointment."""
    date_input = click.prompt("Enter appointment date (YYYY-MM-DD)")
    
    # Convert the date input to a datetime object
    try:
        date = datetime.strptime(date_input, "%Y-%m-%d").date()
    except ValueError:
        click.echo("Invalid date format. Please use YYYY-MM-DD.")
        return

    reason = click.prompt("Enter appointment reason")

    clients = session.query(Client).all()
    animals = session.query(Animal).all()
    vets = session.query(Veterinarian).all()

    click.echo("Available Clients:")
    for client in clients:
        click.echo(f"ID: {client.id}, Name: {client.name}")

    click.echo("Available Animals:")
    for animal in animals:
        click.echo(f"ID: {animal.id}, Name: {animal.name}")

    click.echo("Available Veterinarians:")
    for vet in vets:
        click.echo(f"ID: {vet.id}, Name: {vet.name}")

    client_id = click.prompt("Enter the client's ID", type=int)
    animal_id = click.prompt("Enter the animal's ID", type=int)
    veterinarian_id = click.prompt("Enter the veterinarian's ID", type=int)

    appointment = Appointment(date=date, reason=reason, client_id=client_id, animal_id=animal_id, veterinarian_id=veterinarian_id)
    session.add(appointment)
    session.commit()
    click.echo("Appointment added.")


@cli.command('add-prescription')
def add_prescription():
    """Add a new prescription."""
    medication = click.prompt("Enter medication name")
    dosage = click.prompt("Enter dosage")

    animals = session.query(Animal).all()
    if animals:
        click.echo("Available Animals:")
        for animal in animals:
            click.echo(f"ID: {animal.id}, Name: {animal.name}")
        animal_id = click.prompt("Enter the animal's ID", type=int)
    else:
        click.echo("No animals available.")
        return

    prescription = Prescription(medication=medication, dosage=dosage, animal_id=animal_id)
    session.add(prescription)
    session.commit()
    click.echo("Prescription added.")

@cli.command('list-clients')
def list_clients():
    """List all clients."""
    clients = session.query(Client).all()
    click.echo("\nClients:")
    for client in clients:
        click.echo(f"ID: {client.id}, Name: {client.name}, Email: {client.email}, Phone: {client.phone}")

@cli.command('list-veterinarians')
def list_veterinarians():
    """List all veterinarians."""
    veterinarians = session.query(Veterinarian).all()
    click.echo("\nVeterinarians:")
    for veterinarian in veterinarians:
        click.echo(f"ID: {veterinarian.id}, Name: {veterinarian.name}")

@cli.command('list-specializations')
def list_specializations():
    """List all specializations."""
    specializations = session.query(Specialization).all()
    click.echo("\nSpecializations:")
    for specialization in specializations:
        click.echo(f"ID: {specialization.id}, Name: {specialization.name}")

@cli.command('list-animals')
def list_animals():
    """List all animals."""
    animals = session.query(Animal).all()
    click.echo("\nAnimals:")
    for animal in animals:
        owner_name = animal.owner.name if animal.owner else "No owner"
        click.echo(f"ID: {animal.id}, Name: {animal.name}, Species: {animal.species}, Breed: {animal.breed}, Age: {animal.age}, Owner: {owner_name}")

@cli.command('list-appointments')
def list_appointments():
    """List all appointments."""
    appointments = session.query(Appointment).all()
    click.echo("\nAppointments:")
    for appointment in appointments:
        vet_name = appointment.veterinarian.name
        animal_name = appointment.animal.name
        client_name = appointment.client.name
        click.echo(f"Appointment ID: {appointment.id}, Veterinarian: {vet_name}, Animal: {animal_name}, Client: {client_name}, Date: {appointment.date}, Reason: {appointment.reason}")

@cli.command('list-prescriptions')
def list_prescriptions():
    """List all prescriptions."""
    prescriptions = session.query(Prescription).all()
    click.echo("\nPrescriptions:")
    for prescription in prescriptions:
        animal_name = prescription.animal.name
        click.echo(f"Prescription ID: {prescription.id}, Medication: {prescription.medication}, Dosage: {prescription.dosage}, Animal: {animal_name}")

@cli.command('delete-client')
def delete_client():
    """Delete a client."""
    client_id = click.prompt("Enter the ID of the client to delete", type=int)
    client = session.query(Client).get(client_id)
    if client:
        session.delete(client)
        session.commit()
        click.echo(f"Client ID '{client_id}' deleted.")
    else:
        click.echo(f"Client ID '{client_id}' not found.")

@cli.command('delete-veterinarian')
def delete_veterinarian():
    """Delete a veterinarian."""
    veterinarian_id = click.prompt("Enter the ID of the veterinarian to delete", type=int)
    veterinarian = session.query(Veterinarian).get(veterinarian_id)
    if veterinarian:
        session.delete(veterinarian)
        session.commit()
        click.echo(f"Veterinarian ID '{veterinarian_id}' deleted.")
    else:
        click.echo(f"Veterinarian ID '{veterinarian_id}' not found.")

@cli.command('delete-specialization')
def delete_specialization():
    """Delete a specialization."""
    specialization_id = click.prompt("Enter the ID of the specialization to delete", type=int)
    specialization = session.query(Specialization).get(specialization_id)
    if specialization:
        session.delete(specialization)
        session.commit()
        click.echo(f"Specialization ID '{specialization_id}' deleted.")
    else:
        click.echo(f"Specialization ID '{specialization_id}' not found.")

@cli.command('delete-animal')
def delete_animal():
    """Delete an animal."""
    animal_id = click.prompt("Enter the ID of the animal to delete", type=int)
    animal = session.query(Animal).get(animal_id)
    if animal:
        session.delete(animal)
        session.commit()
        click.echo(f"Animal ID '{animal_id}' deleted.")
    else:
        click.echo(f"Animal ID '{animal_id}' not found.")

@cli.command('delete-appointment')
def delete_appointment():
    """Delete an appointment."""
    appointment_id = click.prompt("Enter the ID of the appointment to delete", type=int)
    appointment = session.query(Appointment).get(appointment_id)
    if appointment:
        session.delete(appointment)
        session.commit()
        click.echo(f"Appointment ID '{appointment_id}' deleted.")
    else:
        click.echo(f"Appointment ID '{appointment_id}' not found.")

@cli.command('delete-prescription')
def delete_prescription():
    """Delete a prescription."""
    prescription_id = click.prompt("Enter the ID of the prescription to delete", type=int)
    prescription = session.query(Prescription).get(prescription_id)
    if prescription:
        session.delete(prescription)
        session.commit()
        click.echo(f"Prescription ID '{prescription_id}' deleted.")
    else:
        click.echo(f"Prescription ID '{prescription_id}' not found.")

if __name__ == "__main__":
    cli()
