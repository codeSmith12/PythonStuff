import turtle

# Pull the two tools we need from the random toolbox
from random import randint, choice

secret = randint(25,100)
print(secret)
pen = turtle.Turtle()
shapes = ["square", "arrow", "circle", "turtle", "triangle", "classic"]
pen.shape( choice(shapes) )
pen.forward(1)
















turtle.done()
