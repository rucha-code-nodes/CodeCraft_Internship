import json

# Contact structure
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __repr__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

# Contact Book Manager
class ContactBook:
    def __init__(self):
        self.contacts = []

    def load_contacts(self):
        try:
            with open("contacts.json", "r") as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = []

    def save_contacts(self):
        with open("contacts.json", "w") as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email, address):
        new_contact = {
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        }
        self.contacts.append(new_contact)
        self.save_contacts()
        print(f"Contact {name} added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for idx, contact in enumerate(self.contacts):
                print(f"{idx+1}. {contact['name']} - {contact['phone']}")

    def search_contact(self, search_term):
        found = False
        for contact in self.contacts:
            if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
                print(contact)
                found = True
        if not found:
            print("Contact not found.")

    def update_contact(self, search_term):
        found = False
        for contact in self.contacts:
            if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
                print(f"Current details: {contact}")
                contact['name'] = input("Enter new name (leave blank to keep current): ") or contact['name']
                contact['phone'] = input("Enter new phone (leave blank to keep current): ") or contact['phone']
                contact['email'] = input("Enter new email (leave blank to keep current): ") or contact['email']
                contact['address'] = input("Enter new address (leave blank to keep current): ") or contact['address']
                self.save_contacts()
                print(f"Contact {contact['name']} updated successfully.")
                found = True
                break
        if not found:
            print("Contact not found.")

    def delete_contact(self, search_term):
        found = False
        for contact in self.contacts:
            if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
                self.contacts.remove(contact)
                self.save_contacts()
                print(f"Contact {contact['name']} deleted successfully.")
                found = True
                break
        if not found:
            print("Contact not found.")

# Main program
def main():
    contact_book = ContactBook()
    contact_book.load_contacts()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")
            address = input("Enter contact address: ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == "2":
            contact_book.view_contacts()

        elif choice == "3":
            search_term = input("Enter contact name or phone to search: ")
            contact_book.search_contact(search_term)

        elif choice == "4":
            search_term = input("Enter contact name or phone to update: ")
            contact_book.update_contact(search_term)

        elif choice == "5":
            search_term = input("Enter contact name or phone to delete: ")
            contact_book.delete_contact(search_term)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

