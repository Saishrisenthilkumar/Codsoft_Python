class Contact:
    def __init__(self, name, phone, email=None, address=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
    def __str__(self):
        return f"{self.name}: {self.phone} {self.email} {self.address}"
class ContactBook:
    def __init__(self):
        self.contacts = []
    def add_contact(self, contact):
        self.contacts.append(contact)
    def view_contacts(self):
        print("Contact List:")
        for contact in self.contacts:
            print(f"{contact.name}: {contact.phone}")
    def search_contacts(self, keyword):
        matching_contacts = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword.lower() in contact.phone.lower():
                matching_contacts.append(contact)
        return matching_contacts
    def update_contact(self, old_contact, new_contact):
        self.contacts.remove(old_contact)
        self.contacts.append(new_contact)
    def delete_contact(self, contact):
        self.contacts.remove(contact)
def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book")
        print("------------")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")
        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue
        if choice == 1:
            name = input("Enter the contact's name: ")
            phone = input("Enter the contact's phone number: ")
            email = input("Enter the contact's email (optional): ")
            address = input("Enter the contact's address (optional): ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
        elif choice == 2:
            contact_book.view_contacts()
        elif choice == 3:
            keyword = input("Enter the name or phone number to search: ")
            matching_contacts = contact_book.search_contacts(keyword)
            for contact in matching_contacts:
                print(contact)
        elif choice == 4:
            name = input("Enter the name of the contact to update: ")
            old_contact = next((contact for contact in contact_book.contacts if contact.name == name), None)
            if old_contact is None:
                print("Contact not found.")
                continue
            phone = input("Enter the updated phone number: ")
            email = input("Enter the updated email (optional): ")
            address = input("Enter the updated address (optional): ")
            new_contact = Contact(name, phone, email, address)
            contact_book.update_contact(old_contact, new_contact)
        elif choice == 5:
            name = input("Enter the name of the contact to delete: ")
            contact = next((contact for contact in contact_book.contacts if contact.name == name), None)
            if contact is None:
                print("Contact")
main()