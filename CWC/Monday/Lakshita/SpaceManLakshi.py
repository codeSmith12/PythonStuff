from random import choice # At the top, we put our imports!


# secret == 'dog'
# letter == 'o'
# dashes = '-o-'
# i = 0,1,2
# secret[0] == 'd'
# secret[1] == 'o'
# secret[2] == 'g'
# dashes[0] == '-'
# dashes[1] == '-'
# dashes[2] == '-'

def updateDashes(dashes, letter, secretWord):
    dashes = list(dashes)
    for i in range(len(secretWord)):
        if letter == secretWord[i]:
            dashes[i] = letter
    return "".join(dashes) # Joins a string with a list,
                           # converting the list to a string

words = ["test", "hello","dog"]

secretWord = choice(words)
print(secretWord)

dashes = '_' * len(secretWord)

tries = 10

guessed = []

while dashes != secretWord and tries != 0:
    print(dashes)
    print("Letters guessed: ", guessed)
    letter = input("Guess a letter: ")

    if len(letter) != 1:
        print("Please only enter 1 character")
    elif letter in secretWord:
        print("You got it!")
        dashes = updateDashes(dashes, letter, secretWord)
        guessed.append(letter)
    else:
        print("There is no", letter)
        guessed.append(letter)
        tries -= 1

if tries == 0:
    print("Sorry, better luck next time. The secret word was:", secretWord)
else:
    print("You got the word! It was", secretWord)
