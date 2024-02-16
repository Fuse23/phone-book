# Phone Book
This is a command-line application for managing a phone book.
It allows users to add, view, edit, and search contacts in the phone book.

## Features:
1. **View Contacts**: Users can view all contacts stored in the phone book.
2. **Add Contact**: Allows users to add a new contact to the phone book by entering contact details.
3. **Edit Contact**: Users can edit an existing contact by providing new details.
4. **Search** Contact: Enables users to search for a contact based on specific 
criteria, such as name, surname, phone number, etc.

## Usage:
Running the Program: Run the main file phone_book as executable or using the Python interpreter.

**Selecting Action**: After launching the program, choose one of the actions by entering 
the corresponding number or keyword:

- 0 or menu: Show the menu with available actions.
- 1 or show: View contacts.
- 2 or add: Add a new contact.
- 3 or edit: Edit an existing contact.
- 4 or search: Search for a contact.
Entering Data: Follow the instructions in the console to add, edit, or search for contacts.

## Running:
Run `create_executed_file.sh` with superuser rights for make executable `phone_book` file

```bash
sudo sh create_executed_file.sh
```

Or run with python

```bash
python3 phone_book
```

## Running tests:
```bash
poetry install
poetry run pytest
```

Or use `pip` for install pytest
```bash
python3 -m pip install pytest
python3 -m pytest
```
