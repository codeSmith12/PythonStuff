# Hello Lakshi!
import turtle
import random
pen = turtle.Turtle()

pen.up()
pen.speed(0)
pen.color("magenta")
pen.shape("turtle")

secret = random.randint(100, 500)

# print(secret)

for i in range(secret):
  pen.goto(random.randint(-400,400), random.randint(-400,400))
  pen.stamp()

guess = "I like coding class!"
tries = 0

while guess != secret:
    guess = int(input("How many turtles are there?"))
    tries += 1
    if guess < secret:
        print("Guess higher")
    elif guess > secret:
        print("Guess lower")
    else:
        print("You got it!!")
print("You got it in", tries, "tries")





turtle.done()
