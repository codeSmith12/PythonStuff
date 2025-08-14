import random

secret = random.randint(0,100)

# CHALLENGE - Count how many times the user guessed
# After the loop ends, print out how many tries
# TIP: tries += 1
tries = 0 # <---------------
guess = ""
while guess != secret:
    guess = int( input("Guess a number: ") )
    tries+=1 # <---------------
    if guess > secret:
        print("Lower")
    elif guess < secret:
        print("Higher")
    else:
        print("You got it!!!")

print("You got it in", tries, "tries.") # <---------------
    

    
