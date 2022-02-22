import turtle, random

screen = turtle.getscreen()
screen.title("Guessing Game")

pen = turtle.Turtle()
pen.color("cyan")
pen.shape("turtle")
pen.up()
pen.shapesize(2,2,2)
pen.speed(0)


theNum = random.randint(100, 400)
# print(theNum)


def goToRandom():
    pen.goto(random.randint(-600, 600), random.randint(-500, 500))


def stampTurtles():
    for i in range(theNum):
        pen.stamp()
        goToRandom()
stampTurtles()

tries = 0
gameOver = False

while gameOver == False:
    guess = int(input("Guess a number: "))
    tries = tries + 1
    if guess < theNum:
        print("Guess higher!")
    elif guess > theNum:
        print("Guess lower!")
    elif guess == theNum:
        if tries == 1:
            print("WOWZERS, you got it on the first try!!!!!!")
        elif tries < 8:
            print("You got it in", tries, "tries. Good job!")
        elif tries < 14:
            print("Wow.... it took you", tries, "tries. Do better next time.")
        # elif tries <= 0:
        #     print("Stop hacking my game broooo")
        else:
            print("You're not even trying, are you?")





        gameOver = True
