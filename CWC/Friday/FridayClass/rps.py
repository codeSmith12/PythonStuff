# rps.py
import random
choices = ["rock", "paper", "scissors"]
playAgain = True
playerScore = 0
botScore = 0
while playAgain: # Runs while playAgain is true
    bot = random.choice(choices)

    print("""
What do you choose:
1) Rock
2) Paper
3) Scissors
    """)
    player = input() # "1"

    if player == "1":
        player = "rock"
    if player == "2":
        player = "paper"
    if player == "3":
        player = "scissors"


    if player == bot:
        print("Tie")

    if player == "rock":
        if bot == "paper":
            print("Paper beats rock. You lose.")
            botScore += 1
        elif bot == "scissors":
            print("Rock beats scissors. You win!")
            playerScore += 1

    elif player == "paper":
        if bot == "rock":
            print("Paper beats rock. You win!")
            playerScore += 1
        elif bot == "scissors":
            print("Scissors beats paper. You lose.")
            botScore += 1

    elif player == "scissors":
        if bot == "paper":
            print("Scissors beats paper. You win!")
            playerScore += 1
        elif bot == "rock":
            print("Rock beats scissors. You lose.")
            botScore += 1
    print(f"Player Score: {playerScore}\nBot Score: {botScore}")
    again = input("Would you like to play again? (Y/N) ")
    if again.upper() != "Y":
         playAgain = False
