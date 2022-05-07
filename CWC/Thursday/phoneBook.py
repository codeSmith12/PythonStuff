class Phonebook:
    # Create a function that will make a phonebook
    def __init__(self):
        # List that holds "Person" objects as contacts
        self.contacts = []
        # Need to get contacts into the list somehow,
        # This function will take a person in,
        # and add the to our list of contacts
    def addContact(self, personObject):
        self.contacts.append(personObject)
    def displayContacts(self):
        for contact in self.contacts:
            contact.displayInfo()




class Person:
    # A function that creates a Person object.
    def __init__(self, firstName, lastName, phoneNumber):
        self.firstName = firstName # Member Variables
        self.lastName = lastName
        self.phoneNumber = phoneNumber

    def displayInfo(self):
        print(f"{self.firstName} {self.lastName} - {self.phoneNumber}")

    def intro(self):
        print(f"Hello, my name is {self.firstName} {self.lastName}! Nice to meet you, my number is {self.phoneNumber}")

Brian = Person("Brian", "Smith", 4669221) # 'Constructor' -> Builds an object
Andrew = Person("Andrew", "Smith", 4561111)
Meleny = Person("Meleny", "Taylor", 8885551)
Carolyn = Person("Meleny", "Smith", 1975246)
Ferox = Person("Ferox", "Smith", 1242069)

# Make a phonebook object
phoneBook = Phonebook()
# Use phonebook object to add person object into phonebook
phoneBook.addContact(Brian)
phoneBook.addContact(Andrew)
phoneBook.addContact(Meleny)
phoneBook.addContact(Carolyn)
phoneBook.addContact(Ferox)
phoneBook.displayContacts()
