contacts = {}

def add_contact(name, phone):
    contacts[name.lower()] = phone

def search_contact(name):
    return contacts.get(name.lower(), "Contact not found.")

def display_contacts():
    for name, phone in contacts.items():
        print(f"{name.title()}: {phone}")

# Example usage:
add_contact("Areeba", "0501234567")
add_contact("Sara", "0509876543")

print(search_contact("sara"))
display_contacts()


