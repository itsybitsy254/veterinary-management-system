# veterinary-management-system

This project is a command-line interface (CLI) app for managing the database of a veterinary clinic. It enables you to add and manage clients, animals, veterinarians, specializations, appointments, and prescriptions using a simple command-based system.

Features

Add new clients, animals, veterinarians, specializations, appointments, and prescriptions.

List clients, veterinarians, specializations, animals, appointments, and prescriptions.

Associate animals with clients, veterinarians with specializations, and appointments between clients, animals, and veterinarians.

Prescriptions are assigned to animals for easy reference.

Requirements

Python 3.x

SQLite database


Setup Instructions
1. Clone the Repository

`***git clone <repository-url>***

**cd veterinary-cli**`

2. Install the Required Packages
The following dependencies are required:

SQLAlchemy (for database ORM)
Click (for creating CLI commands)

`***pip install -r requirements.txt***`

Usage
You can use the CLI tool to manage your veterinary clinic's data. Below are the available commands:

General Command Structure
Copy code
`python -m veterinary.cli [COMMAND]`

Commands
1. Add a Client
Add a new client with their name, email, and phone number.
Copy code
***```python
python -m veterinary.cli add-client
```***


2. Add a Veterinarian
Add a new veterinarian and assign specializations (optional).
Copy code
***python -m veterinary.cli add-veterinarian***

3. Add a Specialization
Add a new veterinary specialization (e.g., Surgery, Dentistry).
Copy code
***python -m veterinary.cli add-specialization***

4. Add an Animal
Add a new animal along with its owner (client), species, breed, and age.
Copy code
***python -m veterinary.cli add-animal***

5. Add an Appointment
Schedule a new appointment for a client’s animal with a veterinarian.
Copy code
***python -m veterinary.cli add-appointment***

6. Add a Prescription
Add a prescription for an animal with the medication name and dosage.
Copy code
***python -m veterinary.cli add-prescription***

7. List Clients
Display all clients in the database.
Copy code
***python -m veterinary.cli list-clients***

8. List Veterinarians
Display all veterinarians in the database.
Copy code
***python -m veterinary.cli list-veterinarians***

9. List Specializations
Display all veterinary specializations.
Copy code
***python -m veterinary.cli list-specializations***

10. List Animals
Display all animals with their owners, species, breed, and age.
Copy code
***python -m veterinary.cli list-animals***

11. List Appointments
Display all appointments with information on the client, animal, and veterinarian.
Copy code
***python -m veterinary.cli list-appointments***

12. List Prescriptions
Display all prescriptions with associated animal details.
Copy code
***python -m veterinary.cli list-prescriptions***


Database Structure
The veterinary.db SQLite database contains the following tables:

clients: Stores client details (name, email, phone number).

veterinarians: Stores veterinarian details (name, specialization IDs).

specializations: Stores veterinary specializations (name).

animals: Stores animal details (name, species, breed, age, and owner).

appointments: Stores appointments between clients, animals, and veterinarians.

prescriptions: Stores medication prescriptions for animals.


