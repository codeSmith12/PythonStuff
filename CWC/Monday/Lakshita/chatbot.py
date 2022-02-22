# chatbot.py












































# Chat bot == Talking robot
# Make a print statement,
# that will introduce our chatbot to the user

def tellJoke():
    jokeAnswer = "Because it had a bluetooth"
    ans1 = input("Why did the computer go to the dentist? ")
    if ans1.lower() == jokeAnswer.lower():
        print("You're good!")
    else:
        print(jokeAnswer + "!!")

def askRiddle():
    riddleAnswer = "newspaper"
    ans2 = input("What is black and blue and red all over? ")
    if ans2.lower() == riddleAnswer.lower():
        print("You're good!")
    else:
        print("A " + riddleAnswer + "!!")

# Input, and output
# Output == information that comes from the computer, and goes OUT to the user
# Input == information that comes from the USER, and goes INTO the computer
print("Hello, my name is Sassbot 2.0, whats yours?") # OUTPUT!!!!
name = input() # "Brian" goes into the name variable
print("Hello", name, "its nice to meet you!") # Print the name variable

print("What is your favorite food?")
food = input()

# You can have what ever response you want for the robots!
# I am only typing examples here, you should add what you want.
# .lower() converts a word to all lowercase...


if food.lower() == "bananas" or food.lower() == "icecream":
    print("I love bananas too!!!")
else:
    print(food, "is gross. I like bananas and icecream.") # DO NOT TYPE JUST THIS PLEASE!!!

botAge = 12 # Integers, WHOLE NUMBER, 1,2,3,4,0,-999,13

age = input("How old are you? ") # String, " string of characters"

if int(age) > botAge:
    print("You must be older than me.")
elif int(age) < botAge:
    print("You must be younger than me.")
else:
    print("We are the same age!!")

joke = input("Would you like to hear a joke? (yes/no)")
if joke.lower() == "yes":
    tellJoke()
else:
    print("Wow.. fine you meany")

riddle = input("Would you like to hear a riddle? (yes/no)")
if riddle.lower() == "yes":
    askRiddle()
else:
    print("Well, I'm not surprised. You don't look like you're good at riddles anyway.")
