# Comment (Ignored by Python)
# This code is where we take information from the user,
# and store it in a variable...
'''
Hello comment

'''

# Windows: ctrl + /
# Mac: cmd + /

# Function - Command... Actions. Collection of instructions that performs an action...
# Call the like function


# Sassbot introduces themself
print("Hello, my name is Mr. Sass Bot the 3rd. Why haven't you told me your name yet!?")
# Sassbot waits for input
# Input == information that goes from the user INto the computer
name = input() # Brian
print(name, "what a lame name that is...")

age = input("Okay, how old are you? ") # NOT INTEGER
# When you take input, it defaults to a "STRING"
age = int(age)
botAge = 12 # int -> integer ?????? WHOLE NUMBER

if age > botAge: # IS TRUE?
    print("Wow you must be ANCIENT!")
elif age < botAge: # else if,
    print("Oh, you're one little baby, aren't ya?")
else:
    print("Oh wow we are the same age?!")

joke = input("Would you like to hear a joke? (y/n) ")

if joke == "y": # if joke(var) == "y"(str)
    answer = input("Why did the computer go to the dentist? ")
    if answer == "It had a bluetooth":
        print("Oh.. You must have heard this one before..")
