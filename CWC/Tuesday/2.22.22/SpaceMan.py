# Get random toolbox
import random
# Create list of words to choose from
words = ["hello","python","sandwich",
            "code","blob","dog","cat",
            "keyboard","whiteboard","coffee",
            "screen", "music", "metal",
            "fun", "mirror", "door", "game", "random",
            "secret", "student", "teacher"]
# Select random word from list !!
secret = random.choice(words) # string
# print secret for debugging
print(secret)
dashes = "-" * len(secret)
# Challenge: Put this in a loop that gives them 10 tries
tries = 10
while tries > 0:
    print(dashes)
    print("Tries:", tries)
    letter = input("Guess a letter: ") # string, "hg"
    if len(letter) != 1:
        print("Please enter 1 letter")
    elif letter in secret:
        print("You got one")
    elif letter not in secret:
        print("Try again")
        tries -= 1 # subtract 1 from current value
