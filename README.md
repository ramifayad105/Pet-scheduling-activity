[README.md](https://github.com/user-attachments/files/23538107/README.md)
# Data Structure Design Choices: Pet Tracker Project

This document outlines the data structure design choices for the **Pet Tracker** application. The project's requirements called for the use of both lists and tuples, and their selection was based on their core characteristics: **mutability (changeability)** and **immutability (fixedness)**.

---

## 1. List: The Primary Dynamic Collection

### What it is used for:
A Python `list` is the primary structure used in each module to hold the main collection of data.

* In `favorite_toys.py`, a list holds all the pet's favorite toys.
* In `vet_appointments.py`, a list holds all the upcoming vet visits.
* In `feeding_schedule.py`, a list holds the different feeding times.
* In `pet_info.py`, a list is used to store the collection of pets being tracked.

### Why a List was chosen:
The primary characteristic of a list is that it is **mutable** (changeable). This is the most critical requirement for our application, which is designed to let users actively manage their pet's information.

The app's core functionality relies on:

* **Adding Data:** Users can add new toys, new appointments, or new feeding times. A list's `.append()` method is perfect for this.
* **Removing Data:** Users can remove a completed appointment, a lost toy, or an old feeding time. A list's `.pop()` or `.remove()` methods are required for this.

A list is the ideal and standard Python structure for a collection that needs to **grow and shrink over time** in response to user actions.



---

## 2. Tuple: The Individual Data Record

### What it is used for:
A `tuple` is used to store a *single, fixed record* that contains multiple related pieces of data. These individual tuples are what we store *inside* our main lists.

* In `pet_info.py`, a single pet's core data is a tuple:
    `('Buddy', 'Golden Retriever', 5)`
* In `vet_appointments.py`, a single appointment is a tuple:
    `('2025-11-15', 'Annual Checkup')`
* In `favorite_toys.py`, a single toy and its type is a tuple:
    `('Squeaky Hedgehog', 'Plush Toy')`
* In `feeding_schedule.py`, a single feeding event is a tuple:
    `('8:00 AM', '1 cup kibble')`

### Why a Tuple was chosen:
The primary characteristic of a tuple is that it is **immutable** (unchangeable). This provides data integrity and makes our code's intent clearer.

* **Groups Fixed Data:** A pet's name, breed, and age are a single, logical unit. An appointment's date and its reason belong together. A tuple groups these related items perfectly.
* **Prevents Accidental Changes:** Using a tuple makes it impossible to accidentally change *only* the date of an appointment or *just* the name of a pet. To "edit" a record, our code must purposefully remove the old tuple and add a new, complete one. This is a safer and more deliberate process.
* **Signifies Intent:** By using a tuple, we signal to other developers (and our future selves) that "this is a fixed record; it is not meant to be modified in-place."

In summary, we use **mutable lists** as containers for our **immutable tuples**, which serve as the records within those containers.
