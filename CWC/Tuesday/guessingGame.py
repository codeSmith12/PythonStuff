import turtle

# Pull the two tools we need from the random toolbox
from random import randint, choice

secret = randint(25,100)
pen = turtle.Turtle()
# Maybe ask the user what background color they want, then use it.
turtle.bgcolor("black")
pen.color("spring green")
shapes = ["square", "arrow", "circle", "turtle", "triangle", "classic"]
pen.shape(choice(shapes))
pen.forward(1)
pen.up()
pen.speed(0)

# Draws "secret" amount of objects on the screen
for i in range(secret):
    pen.goto( randint(-400,400) , randint(-400,400) )
    pen.stamp()


tries = 0
guess = 0 # Created variable so we can use in while condition
while guess != secret:
    # Input gives us back a string, always...
    guess = input("How many objects are there? ")
    guess = int(guess) # convert the guess to a number
    tries += 1
    if guess > secret:
        print("Guess lower")
    if guess < secret:
        print("Guess higher")

print(f"You got it in {tries} tries!!")













turtle.done()
