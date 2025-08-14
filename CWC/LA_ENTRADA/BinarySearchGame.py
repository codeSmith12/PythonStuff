


# Program that guesses your number

print("Let's play a game. You will think of a number and I will try to guess it.")
print("Before we start, I want you to give me the range of numbers we'll be playing with.")
minimum = int(input("What is the minimum number you can choose from? "))
maximum = int(input("What is the maximum number you can choose from? "))

print(f"We will play a game where you choose a number between {minimum} and {maximum}. I will make a guess and you have to tell me to guess 'higher' or 'lower', or 'correct'\n")
# 333
answer = ""
tries = 0
while answer != "correct":
    guess = int(minimum +  (maximum-minimum) / 2 )
    answer = input(f"\nIs your number higher or lower than {guess}? ")
    tries += 1
    if answer == "higher":
        minimum = guess
    elif answer == "lower":
        maximum = guess

print(f"You number was {guess}! It took me {tries} tries to find it. Good game :)")