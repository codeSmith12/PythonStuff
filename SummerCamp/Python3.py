import tkinter as tk
import time

# class Smith:
#     def __init__(self, firstName, age):
#         self.lastName = "Smith"
#         self.firstName = firstName
#         self.age = age
#         self.hairColor = "Blonde"
#     def intro(self):
#         print("Hello my name is", self.firstName, " and I am ", self.age, "years old.")
#
# Brian = Smith("Brian", 28)
# Brian.intro()



window = tk.Tk()
window.title("Pong Game")
window.geometry("300x300")
windowWidth = 300
windowHeight = 300
canvas = tk.Canvas(window, width=windowWidth, height=windowHeight)
canvas.pack()
ballSpeed = 5
width = 100
height = 40

class Paddle:
    def __init__(self, canvas, color):
        self.x = 0
        self.canvas = canvas
        self.paddle = canvas.create_rectangle(0, 0, width, height, fill="red")
        self.canvas.move(self.paddle, (windowWidth / 2) - width / 2,
                    (windowHeight / 2) - height / 2)
        self.canvas.bind_all('<KeyPress-Left>', self.goLeft)
        self.canvas.bind_all('<KeyPress-Right>', self.goRight)

    def goLeft(self, event):
        print("Moving left!")
        self.x = -10

    def goRight(self, event):
        print("Moving right!")
        self.x = 10

    def updatePosition(self):
        self.canvas.move(self.paddle, self.x, 0)
        pos = self.canvas.coords(self.paddle)
        if pos[0] <= 1:
            self.x = 0
        elif pos[2] >= windowWidth:
            self.x = 0

class Ball:
    def __init__(self, canvas, color):
        self.x = ballSpeed
        self.y = ballSpeed
        self.canvas = canvas
        self.ball = self.canvas.create_oval(0,0,20,20,fill=color)
        self.canvas.move(self.ball, windowWidth/2, windowHeight/4)
    def updatePosition(self):
        self.canvas.move(self.ball, self.x, self.y)
        pos = self.canvas.coords(self.ball)
        if pos[0] <= 0:
            self.x=ballSpeed
        if pos[1] <= 0:
            self.y = ballSpeed
        if pos[2] >= windowWidth:
            self.x = -ballSpeed
        if pos[3] >= windowHeight:
            self.y = -ballSpeed




ball = Ball(canvas, "blue")
paddle = Paddle(canvas, "red")


# INFINITE LOOP
while True:
    #canvas.move(paddle, x, y)
    ball.updatePosition() # <---------------------------
    paddle.updatePosition()
    window.update()
    time.sleep(.1)
