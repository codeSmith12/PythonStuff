import tkinter

class Paddle:
    def __init__(self):
        pass

class Ball:
    def __init__(self, fill_color):
        self.id = canvas.create_oval(BALL_START_X, BALL_START_Y, BALL_START_X+BALL_DIAMETER, BALL_START_Y+BALL_DIAMETER, fill=fill_color, outline=fill_color)
        self.x = 50
        self.y = 50
        



# Constants 
WIDTH = 1000
HEIGHT = 800
BALL_DIAMETER = 30
LINE_WIDTH = 4
PADDLE_LENGTH = 100
PADDLE_WIDTH = 20
BALL_START_X = WIDTH/2 - BALL_DIAMETER / 2
BALL_START_Y = HEIGHT/2 - BALL_DIAMETER / 2


# Setup Window
window = tkinter.Tk()
window.title("Pong")
window.geometry(f"{WIDTH}x{HEIGHT}")

# Create the canvas
canvas = tkinter.Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Draw line down the middle to separate sides
canvas.create_line(WIDTH/2-LINE_WIDTH/2, 0, WIDTH/2,HEIGHT, width=LINE_WIDTH)

# Create ball

ball = Ball("red")


window.mainloop()