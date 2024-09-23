Veterinary Management System

This project is a command-line interface (CLI) application for managing the database of a veterinary clinic. It enables you to add and manage clients, animals, veterinarians, specializations, appointments, and prescriptions using a simple command-based system.

Features

Add new clients, animals, veterinarians, specializations, appointments, and prescriptions.

List clients, veterinarians, specializations, animals, appointments, and prescriptions.

Associate animals with clients, veterinarians with specializations, and appointments between clients, animals, and veterinarians.

Prescriptions are assigned to animals for easy reference.

Requirements

Python 3.x

SQLite database


Setup Instructions
Clone the Repository

`git clone https://github.com/itsybitsy254/veterinary-management-system.git`

open file directory:
`cd veterinary-management-system/`

Install the Required Packages
The following dependencies are required:

SQLAlchemy (for database ORM)
Click (for creating CLI commands)

Copy code
`pip install -r requirements.txt`


Usage
You can use the CLI tool to manage your veterinary clinic's data. Below are the available commands:
**To access the main menu and run commands automatically, run:**

`python -m veterinary.cli menu`

***Or you can input data manually via:***
Add a new client with their name, email, and phone number.
Copy code
`python -m veterinary.cli add-client`
Add a new veterinarian and assign specializations (optional).
Copy code
`python -m veterinary.cli add-veterinarian`
Add a new veterinary specialization (e.g., Surgery, Dentistry).
Copy code
`python -m veterinary.cli add-specialization`
Add a new animal along with its owner (client), species, breed, and age.
Copy code
`python -m veterinary.cli add-animal`
Schedule a new appointment for a client’s animal with a veterinarian.
Copy code
`python -m veterinary.cli add-appointment`
Add a prescription for an animal with the medication name and dosage.
Copy code
`python -m veterinary.cli add-prescription`
Display all clients in the database.
Copy code
`python -m veterinary.cli list-clients`
Display all veterinarians in the database.
Copy code
`python -m veterinary.cli list-veterinarians`
Display all veterinary specializations.
Copy code
`python -m veterinary.cli list-specializations`
Display all animals with their owners, species, breed, and age.
Copy code
`python -m veterinary.cli list-animals`
Display all appointments with information on the client, animal, and veterinarian.
Copy code
`python -m veterinary.cli list-appointments`
Display all prescriptions with associated animal details.
Copy code
`python -m veterinary.cli list-prescriptions`


Database Structure


clients: Stores client details (name, email, phone number).

veterinarians: Stores veterinarian details (name, specialization IDs).

specializations: Stores veterinary specializations (name).

animals: Stores animal details (name, species, breed, age, and owner).

appointments: Stores appointments between clients, animals, and veterinarians.

prescriptions: Stores medication prescriptions for animals.


