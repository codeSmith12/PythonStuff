from random import randint
import turtle

class GuessingGame:
    def __init__(self, min, max):
        self.pen = turtle.Turtle()
        self.min = min
        self.max = max
        self.secret = randint(min, max)
        self.run = True
        self.tries = 0

        self.pen.speed(0)
        self.pen.shape("turtle")
        self.pen.color("cyan")
        self.pen.up()
        self.pen.hideturtle()
        turtle.bgcolor("black")


    def displayObjects(self):
        for i in range(self.secret):
            self.pen.goto(randint(-400,400), randint(-400,400))
            self.pen.stamp()


    def playGame(self):
        self.pen.clear()
        self.displayObjects()

        while self.run:
            guess = int(input("How many turtles are there? "))
            self.tries += 1

            if guess < self.secret:
                print("Guess higher")
            elif guess > self.secret:
                print("Guess lower")
            else:
                print(f"You got it in {self.tries} tries.")
                self.run = False









game = GuessingGame(200,400)
game.playGame()
turtle.done()
