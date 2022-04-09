# # Gives us the tools to use randomization in our programs
# import random
#
# # Generates a random number between the given range
# random.randint(0, 500)
#
# # Makes a list of different strings that represent colors
# colors = [
# "teal",
# "red",
# "black"
# ]
# # chooses a random color from the list
# random.choice(colors)
# # What is a variable?
#
# # Answer Given:
# # We can use them to count stuff
# # They store data, and can be changed (+1)
#
# # How do I create a variable in python?
# # nameOfVariable = Value (number or word)
#
# score = 0
# # Increase the value of score by 1
# score = score + 1
# # Add 1 to score - shorthand way
# score += 1
#
# x = 10
#
# # Data types:
# # What is the data type?
#
# x = 10 # integer, whole number!
# x = "10" # string!!!!
#
# # Taking in information:
# #age = input("How old are you?") # input stops program and takes information, stores in variable
# # input command returns a string, we cant do math with strings
# # So we must convert string to integer using int()
#
# choice = input("ask the question you want....")
# age = int(input("How old are you?"))
#
# # Conditionals:
#
# botAge = 10
# # if statements, what do they do?
#
# if age == botAge:
#     print("i'm also 10!")
# elif age > botAge:
#     print("youre older than me")
# elif age < botAge:
#     print("You are younger than me")
#
#
# # Nested if statements:
# answer = "red"
# guess = "blue"
#
# # First if statement
# if guess == "blue":
#     print("Blue")
#     if answer == "red": # nested if statement
#         print("red")
# STORAGE SAVES DATA PERMANENTLY
# MEMORY (RAM): HOW MANY PROGRAMS YOU CAN HAVE OPEN AT A TIME

# Creating a variable

# import random
#
# colors = ["green", "blue","red"] # list
# color = random.choice(colors)
# print(color)







import random
# List of strings that the bot can choose from:
choices = ["rock","paper","scissors"]

game = input("Would you like to play a game?")
if game == "y" or game == "yes":
    # Randomly choose for bot
    bot = random.choice(choices)
    # Allow player to choose an option
    player = input("rock, paper or scissors?")
    if player == bot:
        print("Tie game!")

    if player == "rock":
        if bot == "scissors":
            print("You win!")
        elif bot == "paper":
            print("You lose.")

    elif player == "scissors":
        #do more checks here for bot

    elif player == "paper":
        #do more checks here for bot










# # loops:
# # For loop:
# for i in range(10):
#     print(i)
#
# while True:
#     print("FOREVER")
