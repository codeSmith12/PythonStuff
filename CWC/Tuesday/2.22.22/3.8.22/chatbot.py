print("Hello my name is GladBot")
print("What is your name?")
name = input() # MUST HIT ENTER KEY TO END INPUT
# string = "Hello world"
print(name, "what a cool name!")
age = input("How old are you?")
age = int(age) # Converted the string to an integer
# age == "13" -> age == 13
botAge = 12 # <--------- INT

if age > botAge:
    print("You must be older than me.")
if age < botAge:
    print("You must be younger than me.")
if age == botAge:
    print("You must be the same age as me!")
