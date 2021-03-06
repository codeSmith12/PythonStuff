from tkinter import *
from random import randint
import time

class Mouse:
    def __init__(self):
        self.x = randint((MOUSESIZE + HEADSIZE), (WIDTH-HEADSIZE))
        self.x = self.x - (self.x % HEADSIZE)
        self.y = randint(MOUSESIZE, HEIGHT-HEADSIZE)
        self.y = self.y - (self.y % HEADSIZE)
        self.hitBox = canvas.create_rectangle(self.x+MOUSESIZE/2, self.y+MOUSESIZE/2, self.x + MOUSESIZE/2, self.y + MOUSESIZE/2, fill="black" )
        self.id = canvas.create_rectangle(self.x, self.y, self.x + MOUSESIZE, self.y + MOUSESIZE, fill="grey" )

    def respawnMouse(self):
        self.x = randint(MOUSESIZE + HEADSIZE, WIDTH-HEADSIZE)
        self.x = self.x - (self.x % HEADSIZE)
        self.y = randint(MOUSESIZE, HEIGHT-HEADSIZE)
        self.y = self.y - (self.y % HEADSIZE)
        canvas.moveto(self.hitBox, self.x+MOUSESIZE/2, self.y+MOUSESIZE/2)
        canvas.moveto(self.id, self.x, self.y)


    # Fix the parameters ...
    def checkIfTouching(self, snakeTag):
        pos = canvas.coords(self.hitBox)
        snakePos = canvas.coords(snakeTag)
        # print(pos, snakePos)
        # tag = canvas.gettags(snake)
        overlap = canvas.find_overlapping(pos[0],pos[1],pos[2],pos[3])
        if 1 in overlap:
            self.respawnMouse()
            snake.eatMouse()


class Snake:
    def __init__(self):
        self.x = SPEED
        self.y = 0
        self.bodyCount = 0
        self.bodyParts = []
        self.hitBoxes = []
        self.prevPos = []
        self.head = canvas.create_rectangle(WIDTH/2, HEIGHT/2, WIDTH/2 + HEADSIZE, HEIGHT/2 + HEADSIZE, fill="white", tags=('snake'))
        self.tail = self.head
        self.movementLocked = False
        tk.bind("<KeyPress-Up>", self.moveUp)
        tk.bind("<KeyPress-Down>", self.moveDown)
        tk.bind("<KeyPress-Left>", self.moveLeft)
        tk.bind("<KeyPress-Right>", self.moveRight)

    def updatePosition(self):
        global gameOver
        pos = canvas.coords(self.head)
        # self.prevPos = []
        self.prevPos.insert(0, pos)
        if len(self.prevPos) > self.bodyCount+1:
            del self.prevPos[-1]
        canvas.move(self.head, self.x, self.y)
        for i in range(len(self.bodyParts)):
                canvas.moveto(self.hitBoxes[i], self.prevPos[i][0]+HEADSIZE//2, self.prevPos[i][1]+HEADSIZE//2)
                canvas.moveto(self.bodyParts[i], self.prevPos[i][0], self.prevPos[i][1])

        # If a body hitbox is enclosed within the head, game over
        if len(canvas.find_enclosed(pos[0],pos[1],pos[2],pos[3])) > 1:
            gameOver = True

        self.movementLocked = False
        if pos[0] < 0:
            gameOver = True
        elif pos[1] < 0:
            gameOver = True
        elif pos[2] >= WIDTH:
            gameOver = True
        elif pos[3] >= HEIGHT:
            gameOver = True

    def moveUp(self,key):
        if self.y != SPEED and not self.movementLocked:
            self.y = -SPEED
            self.x = 0
            self.movementLocked = True
    def moveDown(self,key):
        if self.y != -SPEED and not self.movementLocked:
            self.y = SPEED
            self.x = 0
            self.movementLocked = True
    def moveLeft(self,key):
        if self.x != SPEED and not self.movementLocked:
            self.x = -SPEED
            self.y = 0
            self.movementLocked = True
    def moveRight(self,key):
        if self.x != -SPEED and not self.movementLocked:
            self.x = SPEED
            self.y = 0
            self.movementLocked = True

    def getPos(self):
        return canvas.coords(self.head)
    def getSelf(self):
        return self.head
    def eatMouse(self):
        global score
        pos = canvas.coords(self.head)
        hitBox = canvas.create_rectangle(self.prevPos[-1][0]+HEADSIZE//2, self.prevPos[-1][1]+HEADSIZE//2, self.prevPos[-1][0]+HEADSIZE//2, self.prevPos[-1][1]+HEADSIZE//2, fill="black")
        part = canvas.create_rectangle(self.prevPos[-1][0], self.prevPos[-1][1], self.prevPos[-1][2], self.prevPos[-1][3], fill="white")
        self.hitBoxes.append(hitBox)
        self.bodyParts.append(part)
        self.bodyCount += 1
        score+=1
        canvas.itemconfig(scoreText, text=score) # Update scoretext with new score

def drawGrid():
    cellWidth = WIDTH // COLS
    cellHeight = HEIGHT // ROWS
    for i in range(1, ROWS):
        canvas.create_line(0, i*cellHeight, WIDTH, i*cellHeight, fill="ivory3")
    for i in range(COLS):
        canvas.create_line(i*cellWidth, 0, i*cellWidth, HEIGHT, fill="ivory3")





# GAME CONSTANTS
tk = Tk()
tk.title("Snake")
WIDTH=800
HEADSIZE=25
HEIGHT=800
# ENSURE THE DIMENSIONS OF THE GAME WILL SCALE CORRECTLY
assert WIDTH % HEADSIZE == 0, "Width does not divide evenly by Headsize of snake"
assert HEIGHT % HEADSIZE == 0, "Height does not divide evenly by Headsize of snake"
ROWS = HEIGHT//HEADSIZE
COLS = WIDTH//HEADSIZE

TAILSIZE=18
MOUSESIZE=HEADSIZE
SPEED = HEADSIZE
TICK = 0.15


tk.geometry(f"{WIDTH}x{HEIGHT}")
tk.configure(bg="black")

# Controls the menu's loop
global beginGame
beginGame = True


def playGame():
    global beginGame
    beginGame = True

def main():
    global canvas, snake, mouse, scoreText, score, gameOver, beginGame
    # Maybe create 1 canvas outside of main? Hmmmmm
    beginGame = True
    canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="black")
    canvas.pack()

    snake = Snake()
    drawGrid()
    mouse=Mouse()
    score = 0
    scoreText = canvas.create_text(WIDTH//2-HEADSIZE/2, (HEIGHT//ROWS)/2, text=score, fill="white")

    gameOver = False
    # Game Loop - updates the window with newly moved objects
    while not gameOver:
        snake.updatePosition()
        mouse.checkIfTouching(snake.getSelf())
        tk.update()
        time.sleep(TICK)

    # reset the board
    canvas.delete("all") # is it possible for use to press a button,
    del canvas, snake, mouse, scoreText, gameOver
    # that will delete the current canvas and make another? I think so..
    tk.update()
    displayMenu(score)

def displayMenu(score):
    global beginGame
    beginGame = False

    # Open file and grab the current highscore
    scoreFile = open("score.txt", "r")
    highScore = scoreFile.readline() # I think it gives a string back
    # Close file immediately so we can open again for writing
    scoreFile.close()

    # If the file didnt have a highscore yet, then create a new one.
    if len(highScore) == 0:
        highScore = 0
    # Check if new score is greater than our current HIGHSCORE
    # if so set new highscore...
    if int(highScore) < score:
        highScore = score

    # Open highscore file in write mode, and insert the new highscore into the file.
    scoreFile = open("score.txt", "w")
    scoreFile.write(str(highScore))
    scoreFile.close()

    curScoreLabel = Label(tk, text=f"Score: {score}", width=16, height=2, bg="black", fg="gold", font=("Helvetica",32, "bold")).place(relx=.5, rely=.25, anchor=CENTER)
    highScoreLabel = Label(tk, text=f"High Score: {highScore}", width=16, height=2, bg="black", fg="gold", font=("Helvetica",32, "bold")).place(relx=.5, rely=.35, anchor=CENTER)
    playBtn = Button(tk, text="Play Again", width=WIDTH//60, height=2, bg="grey", fg="black", font=("Helvetica",20, "bold"), command=playGame)
    playBtn.place(relx=.5, rely=.5, anchor=CENTER)
    while not beginGame:
        tk.update()
        time.sleep(.1)
    del curScoreLabel, highScoreLabel, playBtn
    for widget in tk.winfo_children():
        widget.destroy()
    tk.update()
    main()

main()
