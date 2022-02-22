class Person:
    def __init__(self): # What is self?
        self.firstName = "Sally" # Attribute
        self.lastName = "Sandoval" # Attribute

    def sayHello(self): # Method
        print("Hello! My name is", self.firstName, self.lastName)
Sally = Person()
Sally.sayHello()
