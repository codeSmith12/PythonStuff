# Define what a person is in our program

# Homework
'''
Homework:
Using classes, objectify 3-5 things around your house. You can use print statements to describe the actions these items perform.
For example:

class Lamp:
    def __init__(self):
        self.lightbulb = "32W SmartLight"
        self.is_on = False
        self.wifi_connected = true
    def turn_on(self):
        self.is_on = True
        print("Light is turning on")
    def turn_off(self):
        self.is_on = False
        print("Light is turning off")

class Remote:
    def __init__(self):
        self.buttons = [1,2,3,4,5,6,7,8,9]
    def change_channel(self, channel):
        print("Changing channel to ", channel)
        

class Phone:
    def __init__(self):
        self.buttons = [0,1,2,3,4,5,6,7,8,9]
    def call(self, number):
        print("Calling phone number", number)
    

'''


'''


'''
class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old!")
    def toStr(self):
        return f"Name:{self.name}\nAge:{self.age}"

# Create person objects
person1 = Person("Brian", 32)
person2 = Person("Jake", 29)
person3 = Person("Dylan", 33)
person4 = Person("Ian", 34)

# Group objects together
people = [person1, person2, person3, person4]

for person in people:
    person.greet()
