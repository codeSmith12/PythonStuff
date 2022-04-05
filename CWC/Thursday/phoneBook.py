class Smith:
    # A function that creates a Smith object.
    def __init__(self, firstName):
        self.firstName = firstName # Member Variables
        self.lastName = "Smith"
    def intro(self):
        print(f"Hello, my name is {self.firstName} {self.lastName}! Nice to meet you.")

brian = Smith("Brian") # 'Constructor' -> Builds an object
brian.intro() # Call our intro function

andrew = Smith("Andrew")
andrew.intro()
