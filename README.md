Veterinary Management System

This project is a command-line interface (CLI) application for managing the database of a veterinary clinic. It enables you to add and manage clients, animals, veterinarians, specializations, appointments, and prescriptions using a simple command-based system.

Features

Add new clients, animals, veterinarians, specializations, appointments, and prescriptions.

List clients, veterinarians, specializations, animals, appointments, and prescriptions.

Associate animals with clients, veterinarians with specializations, and appointments between clients, animals, and veterinarians.

Prescriptions are assigned to animals for easy reference.

Requirements

Python 3.^

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


Database Structure


clients: Stores client details (name, email, phone number).

veterinarians: Stores veterinarian details (name, specialization IDs).

specializations: Stores veterinary specializations (name).

animals: Stores animal details (name, species, breed, age, and owner).

appointments: Stores appointments between clients, animals, and veterinarians.

prescriptions: Stores medication prescriptions for animals.


