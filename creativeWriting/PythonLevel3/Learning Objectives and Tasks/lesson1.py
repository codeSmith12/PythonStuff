'''
Python Level 3 - Lesson 1 - Object Oriented Programming (OOPs I Did It Again)

Objectives:
    - Learn what the benefits are of an OOP approach
    - Learn why we would group data together inside of objects
    - Touch on the subject of encapsulation
    - Learn what the syntax is for creating an object
    - How to access data, and call member functions
    - Enlighten students that they've been using it all along (Show them turtle, random, math)

Tasks:
    - Create a Person object
    - Understand what an init function does. Example on slides might be initializing a game, setting scores to 0 and such
    - Using this class, create 3-5 Person objects, with different data
    - Understand how to access an objects data (person1.name)
    - Create a member function that allows the person to introduce themselves

Homework:
    Practice objectifying objects around the house
    Each object needs to have at least 1 member variable and 1 member function, more is highly encouraged
    Students are encouraged to think of what data might go into these member functions, and what their output might be
    It is okay at this point to use print statements to describe what the function would do

Homework Example:
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
        
Note: member functions are just like normal functions in that they can take in parameters.
Apply this thinking to your objects. 
class Phone:
    def __init__(self):
        self.buttons = [0,1,2,3,4,5,6,7,8,9]
    def call(self, number):
        print("Calling phone number", number)


'''
