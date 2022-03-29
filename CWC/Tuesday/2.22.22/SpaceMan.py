# Get random toolbox
import random
# immutable

def updateDashes(letter, dashes, secret):
    dashes = list(dashes) # converted the string to a list
    # i = 0,1,2
    for i in range(len(secret)):
        if letter == secret[i]:
            dashes[i] = letter
    # Coverts the list back to a string...
    dashes = "".join(dashes) # Returns a string..
    return dashes



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
dashes = "-" * len(secret)
# Challenge: Put this in a loop that gives them 10 tries
tries = 10
while tries > 0 and dashes != secret:
    print(dashes)
    print("Tries:", tries)
    letter = input("Guess a letter: ") # string, "hg"
    if len(letter) != 1:
        print("Please enter 1 letter")
    elif letter in secret:
        print("You got one")
        # save the changes you made to dashes by setting dashes = to function
        dashes = updateDashes(letter, dashes, secret)
    elif letter not in secret:
        print("Try again")
        tries -= 1 # subtract 1 from current value
