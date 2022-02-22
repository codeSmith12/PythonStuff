# output
print("Hello, my name is Optimist Prime.")
print("What is your name, my friend?")
name = input() # name == "Brian"
print("Hello", name)
# input with question asked inside

age = input("How old are you? ") # "28" string
age = int(age) # integer, whole number, 28

botAge = 12

 # Convert to elif, else
if age > botAge: # 13 -> infinity
    print("You must be older than me.")
elif age < botAge: # 11 -> -infinity
    print("You must be younger than me.")
else: # 12
    print("We must be the same age!!!")
# Windows: ctrl + c
# mac: cmd + c
joke = input("Would you like to hear a joke? y/n ")
if joke == "y" or joke == "yes" or joke == "Yes!":
    answer = input("Why did the computer go to the dentist? ")
    if answer == "it had a bluetooth":
        print("You're good!!!")
    else:
        print("It had a bluetooth!!!")
else:
    print("Good, because you would have died laughing!")

# Windows: ctrl + v
# mac: cmd + v
riddle = input("Would you like to hear a riddle? y/n ")
if riddle == "y" or riddle == "yes" or riddle == "Yes!":
    answer = input("What gets wetter the more it dries?")
    if answer == "towel":
        print("Good job!")
    else:
        print("A towel!!")
else:
    print("It was a good one though :(")
