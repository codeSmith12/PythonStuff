# What is a variable?

# Answer Given:
# We can use them to count stuff
# They store data, and can be changed (+1)

# How do I create a variable in python?
# nameOfVariable = Value (number or word)

x = 10

# Data types:
# What is the data type?

x = 10 # integer, whole number!
x = "10" # string!!!!

# Taking in information:
#age = input("How old are you?") # input stops program and takes information, stores in variable
# input command returns a string, we cant do math with strings
# So we must convert string to integer using int()
age = int(input("How old are you?"))

# Conditionals:

botAge = 10
# if statements, what do they do?

if age == botAge:
    print("i'm 10")
if age > botAge:
    print("youre older than me")
elif age < botAge:
    print("You are younger than me")

# Nested if statements:
answer = "red"
guess = "blue"

# First if statement
if guess == "blue":
    print("Blue")
    if answer == "red": # nested if statement
        print("red")
