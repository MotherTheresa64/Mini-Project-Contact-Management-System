import re
import json
contacts = {}
# Function to add a new contact unless it already exists
def add_contact():
    print("\nAdding a new contact:")
    unique_id = input("Enter unique identifier (e.g., email or phone number, can be anything): ")
    if unique_id in contacts:
        print("Contact with this identifier already exists!")
        return
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email address: ")
    additional_info = input("Enter additional information: ")
    contacts[unique_id] = {
        'Name': name,
        'Phone': phone_number,
        'Email': email,
        'Additional': additional_info
    }
    print("Contact added successfully!")
# Function to edit any contacts via their unique identifier on file unless they don't exist
def edit_contact():
    print("\nEditing an existing contact:")
    unique_id = input("Enter unique identifier of the contact to edit: ")
    if unique_id not in contacts:
        print("Contact not found!")
        return
    print("Current details:")
    print_contact(unique_id)
    name = input("Enter new name (press Enter to keep current): ")
    phone_number = input("Enter new phone number (press Enter to keep current): ")
    email = input("Enter new email address (press Enter to keep current): ")
    additional_info = input("Enter new additional information (press Enter to keep current): ")
    if name:
        contacts[unique_id]['Name'] = name
    if phone_number:
        contacts[unique_id]['Phone'] = phone_number
    if email:
        contacts[unique_id]['Email'] = email
    if additional_info:
        contacts[unique_id]['Additional'] = additional_info
    print("Contact updated successfully!")
# Function to delete any contact on file via their unique identifier
def delete_contact():
    print("\nDeleting a contact:")
    unique_id = input("Enter unique identifier of the contact to delete: ")
    if unique_id not in contacts:
        print("Contact not found!")
        return
    del contacts[unique_id]
    print("Contact deleted successfully!")
# Function to search for a specific contact via the unique identifier
def search_contact():
    print("\nSearching for a contact:")
    unique_id = input("Enter unique identifier of the contact to search: ")
    if unique_id in contacts:
        print_contact(unique_id)
    else:
        print("Contact not found!")
# Function to display all contacts 
def display_contacts():
    print("\nAll contacts:")
    if not contacts:
        print("No contacts found.")
    else:
        for unique_id in contacts:
            print_contact(unique_id)
# Function that prints the contact via their unique ID and provides a specific format
def print_contact(unique_id):
    print(f"Identifier: {unique_id}")
    print(f"Name: {contacts[unique_id]['Name']}")
    print(f"Phone: {contacts[unique_id]['Phone']}")
    print(f"Email: {contacts[unique_id]['Email']}")
    print(f"Additional Info: {contacts[unique_id]['Additional']}")
    print()
# Function to export our contacts to a specific txt file (couldn't get it to work :/)
def export_contacts():
    if not contacts:
        print("No contacts to export.")
        return
    filename = input("Enter filename to export contacts (e.g., contacts.json): ")
    with open(filename, 'w') as f:
        json.dump(contacts, f, indent=4)
    print(f"Contacts exported successfully to {filename}")
# Function to import contacts from a specific txt file
def import_contacts():
    filename = input("Enter filename to import contacts from (e.g., contacts.json): ")
    try:
        with open(filename, 'r') as f:
            imported_contacts = json.load(f)
            contacts.update(imported_contacts)
        print(f"Contacts imported successfully from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found!")
    except json.JSONDecodeError:
        print(f"Invalid JSON format in {filename}. Unable to import.")
# Simple email validation with regex
def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)
# Simple phone number validation with regex (digits, optional hyphens)
def validate_phone_number(phone_number):
    pattern = r'^\d{3}-?\d{3}-?\d{4}$'
    return re.match(pattern, phone_number)
# Calls the function as a whole and gives us choices to choose from every time and runs the chosen function accordingly
def main():
    print("Welcome to the Contact Management System!")
    while True:
        print("\nMenu:")
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Import contacts from a text file (Bonus)")
        print("8. Quit")
        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            import_contacts()
        elif choice == '8':
            print("Thank you for using the Contact Management System!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")
if __name__ == "__main__":
    main()