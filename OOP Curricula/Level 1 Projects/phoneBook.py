
'''
The class could have it's own methods of sorting the entries by First Name,
Last name or ??? Distance from you ???

!!
We could pretend this is a google search in a way, it knows where you are
but can sort the phonebook by who is closest, farthest, or alphabetize by first
or last name


Will write a bunch of methods on how to organize this data
Could also give the students a file filled with entries, so there's so much data
they HAVE to organize it.

!!

Orrrrr





'''

class Person:
    def __init__(self, name, phoneNum, address):
        self.name = name
        self.phoneNum = phoneNum
        self.address = address
        self.distance =
    def displayEntry(self):
        print(f"{self.name} | {self.address} | {self.phoneNum}")


brian = Person("Brian S.", "1-333-444-5555", "4 Privet Drive")
meleny = Person("Meleny T.", "1-333-444-5555", "4 Privet Drive")
dylan = Person("Dylan L.", "1-333-444-5555", "4 Privet Drive")
ian = Person("Ian L.", "1-333-444-5555", "4 Privet Drive")

phoneBook = {
    brian,
    meleny,
    dylan,
    ian
}
