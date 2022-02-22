# OOP = Object Oriented Programming
# vs -> Procedural programming

class Person:
    def __init__(self, firstName, lastName): # initialize ( Create with certain values)
        self.firstName = firstName
        self.lastName = lastName
        # make new member variables for email and address;
        # Email : fake@gmail.com
        # Address Location 4 privet drive
    def greeting(self): # What does every method require?
        print(f"Hello, my name is {self.firstName}. How are you today?")


Brian = Person("Brian", "Smith") # Instantiated an object
andrew = Person("Andrew", "Smith")

Brian.greeting()
