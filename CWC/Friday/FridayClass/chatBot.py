print("Hello, my name is Sassbot 9.0")
print("What is your name?") # Not as efficient
name = input() # Waits for a user to enter some information
print(name, "what a lame name...") # Strings
age = input("How old are you? (Digits only)") # Gives back a string
age = int(age) # Convert age to a number
botAge = 12

if age > botAge:
    print("Wow, you must be ANCIENT!")
elif age < botAge:
    print("You must be a lil bebe!")
else:
    print("Wow, we must be the same age!!")

joke = input("Would you like to hear a joke? Y/N ")
if joke.upper() == "Y":
    answer = input("Why did the computer go to the dentist? ")
    # Check if they got the answer correct, if so, congratulate them
    if answer.lower() == "because it had a bluetooth":
        print("Wow, you got it!!")
    else:
        print("Because it had a bluetooth!!")
else: # Else will catch ANYTHING but the letter y for yes...
    print("Fine, it was too funny for you anyway!")


riddle = input("Would you like to hear a riddle? Y/N ")
if riddle.upper() == "Y":
    answer = input("What gets wetter the more it dries?")
    # Check if they got the answer correct, if so, congratulate them
    if answer.lower() == "a towel":
        print("Wow, you got it!!")
    else:
        print("A towel!!")
else: # Else will catch ANYTHING but the letter y for yes...
    print("Fine, it was too hard for you anyway!")
