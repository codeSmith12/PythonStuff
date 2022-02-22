class Smith:
    def __init__(self, firstName, age, occupation):
        self.firstName = firstName
        self.lastName = "Smith"
        self.age = age
        self.occupation = occupation

    def hello(self):
        print("Hello, my name is", self.firstName, self.lastName, "I am", self.age, "years old, and I am a", self.occupation)

    def brushTeeth(self):
        print(self.firstName, "brushes their teeth vigorously. ARRRR!!")

    def dance(self):
        print(self.firstName, "flails their arms as they dance about. How silly!")





brian = Smith("Brian", 28, "code instructor")
brian.hello()
brian.brushTeeth()
brian.dance()
