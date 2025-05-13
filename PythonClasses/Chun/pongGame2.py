'''
Ball:

Speed / direction

Collision detection
x
y

Paddle:
WIDTH and HEIGHT
SPEED
Collision detection
Color, maybe chosen at begining, maybe shifts over time
Y Movement


'''

import tkinter as tk
import time

class Paddle:
    def __init__(self, player):
        if player:
            self.x = WIDTH // PADDLE_MARGIN - PADDLE_WIDTH//2
            self.y = HEIGHT // 2 - PADDLE_HEIGHT // 2
            canvas.bind_all("<Any-KeyPress>", self.move)
        else:
            self.x = WIDTH * (PADDLE_MARGIN-1) // PADDLE_MARGIN - PADDLE_WIDTH//2
            self.y = HEIGHT // 2 - PADDLE_HEIGHT // 2
            
        self.id = canvas.create_rectangle(self.x, self.y, self.x + PADDLE_WIDTH, self.y + PADDLE_HEIGHT, fill="white")
    def move(self, event):
        if event.keysym == "w":
            canvas.move(self.id, 0,-PADDLE_SPEED)
        elif event.keysym == "s":
            canvas.move(self.id, 0,PADDLE_SPEED)
        
    def getCoords(self):
        return canvas.coords(self.id)

class Ball:
    def __init__(self, color, leftPaddle):
        
        self.x = WIDTH/2 - BALL_SIZE/2
        self.y = HEIGHT/2 - BALL_SIZE/2
        self.x_velocity = X_VEL
        self.y_velocity = Y_VEL
        self.id = canvas.create_oval(self.x, self.y, self.x+BALL_SIZE, self.y+BALL_SIZE, fill=color, outline=color)

        self.leftPaddle = leftPaddle
        
    def update_position(self):
        canvas.move(self.id, self.x_velocity, self.y_velocity)
        self.bounce()

    def bounce(self):
        coords = canvas.coords(self.id)
        # This is for bouncing off walls
        if coords[1] <= 0:
            self.y_velocity *= -1
        elif coords[3] >= HEIGHT:
            self.y_velocity *= -1
        
        # Bounce if paddle is hit
        leftPaddleCoords = self.leftPaddle.getCoords()
        
        print(leftPaddleCoords)
        if coords[0] <= leftPaddleCoords[2] and coords[1] <= leftPaddleCoords[1] and coords[3] >= leftPaddleCoords[3]:
            self.x_velocity *= -1

        


# Constants
WIDTH = 1000
HEIGHT = 800
LINE_WIDTH = 10
BALL_SIZE = 40

PADDLE_WIDTH = 25
PADDLE_HEIGHT = 100
PADDLE_MARGIN = 20
PADDLE_SPEED = 25

TICK = .01*6 # 60 frames per second (I think)
X_VEL = -5
Y_VEL = 5

# Window
window = tk.Tk()
window.geometry(f"{WIDTH}x{HEIGHT}")

# Canvas
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Draw Line
canvas.create_line(WIDTH/2, 0, WIDTH/2, HEIGHT, width=LINE_WIDTH, fill="white")

# Build the left Paddle
playerPaddle = Paddle(True)
# Build the right Paddle
botPaddle = Paddle(False)

# BUILD THE BALL
ball = Ball("red", playerPaddle)


#window.mainloop()

while True:
    ball.update_position()
    window.update()
    time.sleep(TICK)
