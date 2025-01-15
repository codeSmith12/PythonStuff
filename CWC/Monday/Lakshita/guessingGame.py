# Import our 'toolboxes'
import turtle, random
# Pull the pen out of our turtle toolbox
pen = turtle.Turtle()

# Bring pen up so it doesn't draw lines as it teleports around
pen.up()
# Turtle pen settings
pen.speed(0)
pen.color("magenta")
pen.shape("turtle")

# Generate a secret number from 50 to 100
secret = random.randint(50, 100)

# Teleport and stamp a picture of the turtle on the screen
for i in range(secret):
  pen.goto(random.randint(-400,400), random.randint(-400,400))
  pen.stamp()

# We have to create a variable called guess and
# make sure it's NOT set to a value that can be generated randomly (50, 100)
guess = "I like coding class!"
# Keeps track of how many times the player has guessed
tries = 0

# Loop while the game isn't over. While the user hasn't guessed the secret #
while guess != secret:
    # Ask the user for a guess, convert it to an Int
    guess = int(input("How many turtles are there?"))
    # Increment tries
    tries += 1
    # Give them feedback on their guess
    if guess < secret:
        print("Guess higher")
    elif guess > secret:
        print("Guess lower")
    else:
        print("You got it!!")
# After the loop has terminated, give the results.
print("You got it in", tries, "tries")
# Need this to keep the window open after the end is hit.
# Without this the program closes before students can perceive their results.
turtle.done()
