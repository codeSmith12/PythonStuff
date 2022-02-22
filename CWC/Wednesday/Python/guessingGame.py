import turtle, random
pen = turtle.Turtle()
pen.color("cyan")
pen.shape("turtle")
pen.up()
pen.speed(0)


secret = random.randint(50, 1000)


for i in range(secret):
    pen.stamp()
    pen.goto(random.randint(-300,300), random.randint(-300,300))





count = 0
guess = -1

while guess != secret:
    guess = int(input("How many turtles are there?"))
    count += 1
    if guess < secret:
        print("Guess higher")

    elif guess > secret:
        print("Guess lower")

    else:
        print("You got it in", count, "tries!")






















turtle.done()
