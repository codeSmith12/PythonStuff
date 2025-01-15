
import turtle
import random
pen = turtle.Turtle()

pen.up()
pen.speed(0)
pen.color("magenta")
pen.shape("turtle")

secret = random.randint(50, 100)

for i in range(secret):
  pen.goto(random.randint(-200,200), random.randint(-200,200))
  pen.stamp()
  
tries = 0
guess = -1
while guess != secret:
    guess = int(input("How many turtles are there? "))
    tries += 1
    if guess < secret:
        print("Guess higher!")
    elif guess > secret:
        print("Guess lower!")

print(f"You got it in {tries} tries!")

turtle.mainloop()
