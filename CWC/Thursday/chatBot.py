"""
Chatbot - What does it do?

It does things you want it to do.
It runs a conversation
Takes information from the user
makes choices depending on answers
Basic functions of a chatbot:
Displays messages to the user -> using print
How does our bot take information from the user?

"""
# Datatypes
# x = 10 # Variable, integer -> WHOLE NUMBER, 1,2,3,99,-99, NOT 1.0 <- floats point
# # 1.0 * 10 = 10.0 * 10 = 100.0
# this = 12
# x = "this" # == the word this
# words = "Hello" # datatype = STRING!!!
#
# print(Hello) # What is printed?
print("Hello, my name is SassBot 3.0!") # STRING!!!
print("What is your name?")
name = input() # Takes information from the user
print("Hello", name, "it's NOT nice to meet you >:D")
feeling = input("How are you feeling? ") # string

# Type this part
if feeling == "Happy": # Checks if the user has typed "Happy", and if they did
    print("I'm happy too!")
else:
    print("I am also", feeling)
# Have the bot ask how old the user is
age = input("How old are you? ") # Creates a variable that holds a string
age = int(age) # Converting the string "28" into the integer 28 (ACTUAL NUMBER)

# IF THEN ELIF THEN ELSE


if age > 18:
    print("You are an adult!!!")
elif age > 12: # else if (condition)
    print("You are a teenager.")
else: # Catch all
    print("You are a child.")

# Ask the user if they want to hear a joke?
joke = input("Do you want to hear a joke? (Y/N)")
# OPTIMIZE:
# joke == "y" -> "Y"
# joke=="blah" -> "BLAH" Converting a string to all uppercase
if joke.upper() == "Y":
    # Set up the joke and wait for their response
    answer = input("Why can't you give Elsa a balloon?")

    if answer.lower() == "because she'll let it go": # if they get the joke right
        print("Wow, you're good!!")
    else:
        print("Because she'll let it go!!")
else:
    print("The joke was too funny for you anyway!")

riddle = input("Do you want to hear a riddle? (Y/N)")
if riddle.upper() == "Y":
    answer = input("What gets wetter the more it dries? ") # towel
    if answer.lower() == "towel":
        print("You got it!")
    else:
        print("It's a towel, duhh!")
else:
    print("It was a good one though :(")

print("Okay, I have to go now, have a good day!!")
