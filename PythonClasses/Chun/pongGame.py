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
            
        self.isPlayer = player
        self.id = canvas.create_rectangle(self.x, self.y, self.x + PADDLE_WIDTH, self.y + PADDLE_HEIGHT, fill="white")
        self.score = 0
    
    # Score Getters and Setters 
    def getScore(self):
        return self.score

    def increaseScore(self):
        self.score += 1
        if self.isPlayer:
            canvas.itemconfig(playerScore, text=self.score)
        else:
            canvas.itemconfig(botScore, text=self.score)
            
    def move(self, event):
        if self.isPlayer:
            if event.keysym == "w":
                canvas.move(self.id, 0,-PADDLE_SPEED)
            elif event.keysym == "s":
                canvas.move(self.id, 0,PADDLE_SPEED)
        
    def getCoords(self):
        return canvas.coords(self.id)

    def update_position(self, coords):
        if not self.isPlayer:
            paddleCoords = canvas.coords(self.id)
            if paddleCoords[1] >= coords[1]:
                canvas.move(self.id, 0, -BOT_SPEED)
            elif paddleCoords[3] <= coords[3]:
                canvas.move(self.id, 0, BOT_SPEED)


class Ball:
    def __init__(self, color, leftPaddle, rightPaddle):
        self.x = WIDTH/2 - BALL_SIZE/2
        self.y = HEIGHT/2 - BALL_SIZE/2
        self.x_velocity = X_VEL
        self.y_velocity = Y_VEL
        self.id = canvas.create_oval(self.x, self.y, self.x+BALL_SIZE, self.y+BALL_SIZE, fill=color, outline=color)

        self.leftPaddle = leftPaddle
        self.rightPaddle = rightPaddle
        
    def getCoords(self):
        return canvas.coords(self.id)
        
    def update_position(self):
        canvas.move(self.id, self.x_velocity, self.y_velocity)
        self.checkScore()
        self.bounce()

    def checkScore(self):
        coords = canvas.coords(self.id)

        # Check if right side has scored
        if coords[0] <= 0:
            self.rightPaddle.increaseScore()
            self.resetBall()
        elif coords[2] >= WIDTH:
            self.leftPaddle.increaseScore()
            self.resetBall()
        
    def resetBall(self):
        self.x = WIDTH/2 - BALL_SIZE/2
        self.y = HEIGHT/2 - BALL_SIZE/2
        self.x_velocity *=-1 # flip ball direction

        canvas.moveto(self.id, self.x, self.y)
        time.sleep(1)


    def bounce(self):
        coords = canvas.coords(self.id)
        # This is for bouncing off walls
        if coords[1] <= 0:
            self.y_velocity *= -1
        elif coords[3] >= HEIGHT:
            self.y_velocity *= -1
        
        leftPaddleCoords = self.leftPaddle.getCoords()
        rightPaddleCoords = self.rightPaddle.getCoords()
        
        # Bounce if paddle is hit
        if coords[0] <= leftPaddleCoords[2] and coords[1] >= leftPaddleCoords[1] and coords[3] <= leftPaddleCoords[3]:
            # Flip x direction
            self.x_velocity *= -1
            # Shift ball to the right so the ball doesn't get stuck.
            canvas.move(self.id, BALL_SIZE//2, 0)

        # Bounce if paddle is hit
        elif coords[2] >= rightPaddleCoords[0] and coords[1] >= rightPaddleCoords[1] and coords[3] <= rightPaddleCoords[3]:
            # Flip x direction
            self.x_velocity *= -1
            # Shift ball to the left so the ball doesn't get stuck.
            canvas.move(self.id, -BALL_SIZE//2, 0)

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
X_VEL = 10
Y_VEL = 10


# BOT SPEED = 6 for easy,8 for medium and 10 for impossible
BOT_SPEED = 8

# Create the window that holds all of our components.
window = tk.Tk()
window.title("Pong Game")
window.geometry(f"{WIDTH}x{HEIGHT}")


# Create the object we can draw things onto
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

myFont = ('Terminal 50 bold')

# Create text objects for scores
playerScore = canvas.create_text(WIDTH//4, HEIGHT//20, text="0", font=myFont)
# Create text objects for scores
botScore = canvas.create_text(WIDTH*3//4, HEIGHT//20, text="0", font=myFont, fill="white")

# Draw separating line
canvas.create_line(WIDTH/2, 0, WIDTH/2, HEIGHT, width=LINE_WIDTH, fill="white")

# Build the left Paddle
playerPaddle = Paddle(True)

# Build the right Paddle
botPaddle = Paddle(False)

# Build the ball
ball = Ball("red", playerPaddle, botPaddle)


# This is no longer needed now that we want more control over our game loop.
#window.mainloop()

while True:
    ball.update_position()
    botPaddle.update_position(ball.getCoords())
    window.update()
    time.sleep(TICK)
