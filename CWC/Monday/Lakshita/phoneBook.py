import random

# phonebook
class Person:
    # init function is run automatically when creating object
    def __init__(self, firstName, lastName, num):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = num
        self.intros = ["Hey, what's up?", f"Hello, this is {self.firstName}!" ]

    def introduce(self):
        print(random.choice(self.intros))

    def display(self):
        print(f"{self.firstName} {self.lastName} - {self.phoneNumber}")

class Phonebook:
    def __init__(self):
        self.contacts = []

    def addContact(self, person):
        self.contacts.append(person)

    def listContacts(self):
        for contact in self.contacts:
            contact.display()

    def sortByFirstName(self):
        self.contacts.sort(key=lambda x: x.firstName)

    def sortByLastName(self):
        self.contacts.sort(key=lambda x: x.lastName)

    def call(self):
        number = input("Please enter a number to call.\n")
        if len(number) != 7:
            print("Please enter a 7 digit number to call.")
        else:
            number = int(number)
            for contact in self.contacts:
                if contact.phoneNumber == number: # this measns they called correctly
                    print(f"\nConnecting call with {contact.firstName}.")
                    contact.introduce()

Brian = Person("Brian","Smith", 8851353)
Dylan = Person("Dylan","Leal", 8885553)
Meleny = Person("Meleny","Taylor", 6514655)
Lakshi = Person("Lakshita", "Sanghai", 4563245)

phoneBook = Phonebook()

phoneBook.addContact(Brian)
phoneBook.addContact(Dylan)
phoneBook.addContact(Meleny)
phoneBook.addContact(Lakshi)
phoneBook.sortByFirstName()
phoneBook.listContacts()
phoneBook.call()
