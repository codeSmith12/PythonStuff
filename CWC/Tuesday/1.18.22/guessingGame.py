# guessingGame
import turtle, random
pen = turtle.Turtle()
pen.speed(0)
pen.up()
pen.shape("turtle")
secret = random.randint(100, 600)


for i in range(secret):
    # Generate a random location and teleport there
    pen.goto( random.randint(-200,200) , random.randint(-200,200) )
    pen.stamp()

answer = "" # empty string (message)
tries = 0
while answer != secret:
    answer = int(input("How many objects are there?"))
    tries += 1 # adds 1 to the current value.
    if answer < secret:
        print("Guess higher")
    if answer > secret:
        print("Guess lower")

print("You got it in", tries, "tries")







turtle.done()
