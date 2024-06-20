def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print("Contact added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")

def search_contact(contacts):
    search_term = input("Enter Name or Phone Number to search: ")
    found_contacts = [
        (name, details) for name, details in contacts.items()
        if search_term.lower() in name.lower() or search_term in details['phone']
    ]

    if found_contacts:
        for name, details in found_contacts:
            print(f"\nName: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
    else:
        print("No contacts found.")

def update_contact(contacts):
    name = input("Enter the Name of the contact to update: ")
    if name in contacts:
        print("Leave blank to keep current value.")
        phone = input(f"Enter new Phone Number (current: {contacts[name]['phone']}): ") or contacts[name]['phone']
        email = input(f"Enter new Email (current: {contacts[name]['email']}): ") or contacts[name]['email']
        address = input(f"Enter new Address (current: {contacts[name]['address']}): ") or contacts[name]['address']

        contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter the Name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    contacts = {}
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()












