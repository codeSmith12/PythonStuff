import random

moves = ["Rock", "Paper", "Scissors"] # LIST of STRINGS

playAgain = 'y'

playerScore = 0
botScore = 0

while playAgain == 'y':
    botMove = random.choice(moves)
    playerMove = input("Rock, Paper or Scissors? ")

    print("Bot chose", botMove)

    if botMove.lower() == playerMove.lower():
        print("Tie game!")
    elif botMove == "Rock":
        if playerMove.lower() == "scissors":
            print("You lost..")
            botScore += 1
        elif playerMove.lower()== "paper":
            print("You won!")
            playerScore += 1

    elif botMove == "Paper":
        if playerMove.lower() == "scissors":
            print("You won!")
            playerScore += 1
        elif playerMove.lower() == "rock":
            print("You lost..")
            botScore += 1

    elif botMove == "Scissors":
        if playerMove.lower() == "paper":
            print("You lost..")
            botScore += 1
        elif playerMove.lower() == "rock":
            print("You won!")
            playerScore += 1

    print(f"\nPlayer Score: {playerScore}\nBot Score: {botScore}\n")

    playAgain = input("To play again type y: ")

print("Thank you for playing. Good day Sir/Ma'am")
