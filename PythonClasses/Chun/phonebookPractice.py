
class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def print_self(self):
        print(f"{self.name:<10} {self.number:<10}")

    def speak(self):
        print(f"Hello! This is {self.name}")

class Phonebook:
    def __init__(self):
        self.contacts = []
    def add_contact(self,contact):
        self.contacts.append(contact)
    def show_contacts(self):
        print("\nContacts")
        print("-"*20) 
        for contact in self.contacts:
            contact.print_self()
        print("-"*20) 
            
    def call(self, number):
        for contact in self.contacts:
            if number == contact.number:
                contact.speak()






















brian = Contact("Brian", "4084554223")
chun = Contact("Chun", "3405957403")
michael = Contact("Michael", "2234445555")
andrew = Contact("Andrew", "2394958368")

phonebook = Phonebook()
phonebook.add_contact(brian)
phonebook.add_contact(chun)
phonebook.add_contact(michael)
phonebook.add_contact(andrew)

print("\n")
phonebook.show_contacts()

call = input("Would you like to call someone? ")
if call == "yes":
    number = input("Please enter a phone number from the contact list: ")
    phonebook.call(number)

    
