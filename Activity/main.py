from random import randint
import turtle

class Player:
    def __init__(self, type, numGames=1):
        self.averageTries = 0
        self.numGames = numGames
        self.type = type
        self.lowest = 1000
        self.highest = 0
        self.min = 200
        self.max = 1000

    def playGames(self):
        for i in range(self.numGames):
            # Spawn new game object, play
            self.game = GuessingGame(self.min,self.max, self.type)
            tries = self.game.playGame()

            # Track the highest and lowest amount of tries taken
            if tries > self.highest:
                self.highest = tries
            if tries < self.lowest:
                self.lowest = tries

            # Track the average tries
            self.averageTries += tries
            # Free memory, no leaks here!
            del self.game

        # Calculate average and print out results of the games
        self.averageTries /= self.numGames
        return f"\n{self.type} Stats:\nWith a range of {self.min} to {self.max} ({self.max-self.min}) the average tries out of {self.numGames} games was {self.averageTries}, with a low of {self.lowest} tries and a high of {self.highest} tries.\n"

class GuessingGame:
    def __init__(self, min, max, type):
        # Secret game values
        self.min = min
        self.max = max
        self.type = type
        self.secret = randint(min, max)

        # Create and format pen / turtle stuff
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("turtle")
        self.pen.color("cyan")
        self.pen.up()
        self.pen.hideturtle()
        turtle.bgcolor("black")

        # Game variables
        self.run = True
        self.tries = 0

    def displayObjects(self):
        for i in range(self.secret):
            self.pen.goto(randint(-400,400), randint(-400,400))
            self.pen.stamp()

    def playGame(self):
        print(f"\n{self.type} game\n---------------------")
        if self.type != "Computer":
            self.pen.clear()
            self.displayObjects()

        curMin = self.min
        curMax = self.max
        lastGuess = 0
        while self.run:
            if self.type != "Computer":
                guess = int(input("How many turtles are there? "))
            else:
                # Calculate computers guess
                guess = curMin + (curMax - curMin)//2
                # Edge cases if the secret is == min or max
                if lastGuess == guess:
                    if guess == self.max-1:
                        guess += 1
                    elif guess == self.min-1:
                        guesss -= 1
                else:
                    lastGuess = guess

                print(f"Computer guess: {guess}")

            self.tries += 1

            if guess < self.secret:
                print("Guess higher")
                if self.type == "Computer":
                    curMin = guess
            elif guess > self.secret:
                print("Guess lower")
                if self.type == "Computer":
                    curMax = guess
            else:
                print(f"---------------------\nYou got it in {self.tries} tries\n---------------------")
                self.run = False
                self.pen.clear()
                return self.tries




# Run computer games
computer = Player("Computer", 2)
compStats = computer.playGames()
# Print computer stats before continuing
print(compStats)
# Run player games
# print("\nHuman games begin: \n")
human = Player("Human", 1)
# print both human and computer stats
print(human.playGames())
print(compStats)


turtle.done()
