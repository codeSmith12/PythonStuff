class Contact:
    def __init__(self, name, number):
        self.name = name 
        self.number = number 
    def display(self):
        print(f"{self.name:<10}: {self.number}")
    def greet(self):
        # write some message USING THEIR NAME!!! (in a formatted string)
        print(f"Hello, my name is {self.name}! What's going on?")


# Make a phonebook class that takes in a list of contacts, and stores it in the object
class Phonebook:
    def __init__(self, contacts):
        self.contacts = contacts
    def display(self):
        for contact in self.contacts:
            contact.display()

Andrew = Contact("Andrew", "1111111111")
Brian = Contact("Brian", "0000000000")
Chris = Contact("Chris", "4444444444")
Carolyn = Contact("Carolyn", "2222222222")
Catherine = Contact("Catherine", "3333333333")


contacts = [Andrew, Brian, Chris, Carolyn, Catherine]

phonebook = Phonebook(contacts)
phonebook.display()