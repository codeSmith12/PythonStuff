class Person:
    # A function that creates a Person object.
    def __init__(self, firstName, lastName, phoneNumber):
        self.firstName = firstName # Member Variables
        self.lastName = lastName
        self.phoneNumber = phoneNumber
    def intro(self):
        print(f"Hello, my name is {self.firstName} {self.lastName}! Nice to meet you, my number is {self.phoneNumber}")

Brian = Person("Brian", "Smith", 4669221) # 'Constructor' -> Builds an object
Brian.intro() # Call our intro function

Andrew = Person("Andrew", "Smith", 4561111)
Andrew.intro()

Meleny = Person("Meleny", "Taylor", 8885551)
Meleny.intro()

Carolyn = Person("Meleny", "Smith", 1975246)
Carolyn.intro()

Ferox = Person("Ferox", "Smith", 1242069)
Ferox.intro()
