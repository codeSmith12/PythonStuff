import random, os
clear = lambda: os.system('cls')
# Open up files, read contents but strip new lines and white spaces
# with open("answers.txt", "r") as answersFile:
#     answers = [line.rstrip() for line in answersFile]

# with open("allowedWords.txt", "r") as wordFile:
#     words = [line.rstrip() for line in wordFile]

print("""
Welcome to a lame version of Wordle. If you guess a letter in the correct
location, it will be displayed in undercase. If you guessed a letter
that's in the word but is in the wrong spot, it will be uppercase.

Good luck!
""")
answers = ["plank", "snake"]
answer = random.choice(answers)
# print(answer)
guess = "0"
letters = "-----"
tries = 6
while guess != answer and tries != 0:
    " ".join(letters)
    print(f"{tries} tries left")
    print(letters)
    guess = input("Guess a 5 letter word: ")
    if len(guess) != 5:
        print("Please guess a 5 letter word.")
    elif guess not in words and guess not in answers:
        print("Word was not found in list.")
    else: # Only check if they followed the rules
        tries -= 1
        if guess in words or guess in answers:
            letters = list(letters)
            # guess = list(guess)
            for i in range(5):
                if guess[i] == answer[i]:
                    letters[i] = guess[i]
                elif guess[i] in answer and guess[i] not in letters:
                    letters[i] = guess[i].upper()

        "".join(letters)
        # "".join(guess)
        clear()
print("You got it!")
