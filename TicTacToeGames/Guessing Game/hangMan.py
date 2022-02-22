import random

words = ["dog","bread","banana","smoothie","heat",
        "melt", "lamp","fan","trees","windows","hammer",
        "keyboard", "clack", "phone", "screen", "enigma"]

correct = random.choice(words)
print(correct)

dashes = '-' * len(correct)
# Start @ tries next time..
while dashes != correct:
    print(dashes)
    letter = input("Guess a letter: ")
    if len(letter) > 1:
        print("Please enter only 1 letter.")
    elif letter in correct:
        print("Good job!")
    elif letter not in correct:
        print("Oof. Try again.")
