# Geometry drawer turtle program:
# rectangle, where, color, size, fill?
# circle
#




class Person:
    def __init__(self, firstName, lastName, age, phoneNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.phoneNumber = phoneNumber

    def introduce(self):
        print(f"Hello, my name is {self.firstName} {self.lastName}, and I am {self.age} years old")

# Create a person object, store in variable called Brian
Brandon = Person("Brandon", "Jung", 9, "409-655-3221") # Constructor -> Calls init function
Brandon.introduce()

Ethan = Person("Ethan", "Rong", 9, "911-991-1111")
Ethan.introduce()

Brian = Person("Brian", "Smith", 29, "444-444-4444")
Brian.introduce()

Andrew = Person("Andrew", "Smith", 35, "222-222-2222")
Carolyn = Person("Carolyn", "Smith", 34, "666-666-6666")
Meleny = Person("Meleny", "Taylor", 31, "252-555-3699")
