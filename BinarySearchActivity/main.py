from random import randint
import turtle

class GuessingGame:
    def __init__(self, min, max):
        self.pen = turtle.Turtle()
        self.min = min
        self.max = max
        self.secret = randint(min, max)

    def displayObjects(self):






game = GuessingGame(200,400)
turtle.done()
