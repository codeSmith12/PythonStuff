# guessingGame.py
import turtle, random
pen = turtle.Turtle()

secret = random.randint(50, 100)

pen.shape("turtle")
pen.color("crimson")
pen.up()
pen.speed(0)

for i in range(secret):
    pen.stamp()             #         x,        y
    pen.goto( random.randint(-200, 200), random.randint(-200,200) )

guess = 0
tries = 0
while guess != secret:
    guess = input("How many turtles are there? ")
    tries += 1
    guess = int(guess)
    if guess > secret:
        print("Guess lower")
    elif guess < secret:
        print("Guess higher")
    else:
        print("You got it!!!")
print(f"You got it in {tries} tries")















turtle.done()
