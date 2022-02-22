from random import choice


def updateDashes(dashes, secret, letter):
    dashes = list(dashes)
    for i in range(len(dashes)):
        if letter == secret[i]:
            dashes[i] = letter
    dashes = "".join(dashes)
    return dashes


# Create list of words to randomly choose from
words = [
    "hello",
    "dog",
    "fish",
    "beyond",
    "infinity",
    "soda",
    "lamp",
    "example",
    "secret",
    "magenta",
    "coding"
]


# Select a word at random
secret = choice(words)
print(secret) # print for testing purposes

# Create dashes variable to hold the unguessed letters
dashes = '-' * len(secret)
print(dashes)

# Create tries variable, holds the number of tries they have left
tries = 10

# Run loop runs while user hasn't won and while they haven't lost
while dashes != secret and tries > 0:
    print(dashes)
    letter = input("Guess a letter: ")
    if len(letter) != 1:
        print("Please enter only 1 letter at a time.")
    elif letter not in secret:
        tries -= 1
        print(f"{letter} is not in the secret word.")
    else:
        print("You got one!")
        dashes = updateDashes(dashes, secret, letter)
