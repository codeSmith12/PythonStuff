from tkinter import *
import time

class Invader:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = INVADERSPEED
        self.id = canvas.create_rectangle(self.x, self.y, self.x + INVADERSIZE, self.y + INVADERSIZE, fill="lime")
        self.destroyed = False

    def updatePosition(self):
        pos = canvas.coords(self.id)
        canvas.move(self.id, self.speed, 0)
        if pos[2] >= WIDTH - 20:
            self.speed *= -1
            canvas.move(self.id, self.speed - 5, DROPSIZE)
        elif pos[0] < 20:
            self.speed *= -1
            canvas.move(self.id, self.speed + 5, DROPSIZE)

        pos = canvas.coords(self.id)
        # Check if touched a bullet
        if len(canvas.find_overlapping(pos[0],pos[1],pos[2],pos[3])) > 1:
            if 1 in canvas.find_overlapping(pos[0],pos[1],pos[2],pos[3]) and not self.destroyed:
                print("game over")
            else:
                canvas.itemconfig(self.id, fill="black")
                self.destroyed = True



class Bullet:
    def __init__(self, pos):
        self.hit = False
        self.id = canvas.create_rectangle(pos[4]-SHIPSIZE//10,pos[1]-SHIPSIZE//2, pos[4]+SHIPSIZE//10, pos[5], fill=BULLETCOLOR, outline="")

class Ship:
    def __init__(self):
        self.id = canvas.create_polygon(WIDTH//2-SHIPSIZE//2, HEIGHT*7//8, WIDTH//2 + SHIPSIZE//2, HEIGHT*7//8, WIDTH//2, HEIGHT*7//8-SHIPSIZE, fill="lime")
        self.bullets = []
        self.shotDelay = 0.0 # double or float
        tk.bind("<KeyPress-Left>", self.moveLeft)
        tk.bind("<KeyPress-Right>", self.moveRight)
        tk.bind("<space>", self.shoot)

    def moveLeft(self, event):
        canvas.move(self.id, -SHIPSPEED, 0)

    def moveRight(self,event):
        canvas.move(self.id, SHIPSPEED, 0)

    def shoot(self, event):
        if self.shotDelay >= SHOTDELAY:
            pos = canvas.coords(self.id)
            bullet = Bullet(pos)
            self.bullets.append(bullet)
            self.shotDelay = 0.0 # reset the counter of when we shot last

    def updateBullets(self):
        self.shotDelay += .05
        for bullet in self.bullets:
            canvas.move(bullet.id, 0, -10)
            pos = canvas.coords(bullet.id)
            # Check if invader(?) touched a bullet
            if len(canvas.find_overlapping(pos[0],pos[1],pos[2],pos[3])) > 1 and not bullet.hit:
                # Make sure the ship isn't the object that touched the bullet.
                if 1 not in canvas.find_overlapping(pos[0],pos[1],pos[2],pos[3]):
                    canvas.itemconfig(bullet.id, fill="black")
                    bullet.hit=True
# Dimensions of space invader are square
WIDTH=600
HEIGHT=WIDTH
SHIPSIZE = 25
SHIPSPEED = 10
BULLETCOLOR="lime"
SHOTDELAY = 1.5
INVADERSPEED = 1.5
INVADERSIZE = 15
SPACEBETWEEN = 75
SPACEABOVE = 50

tk = Tk()
tk.title("Space Invader")
tk.geometry(f"{WIDTH}x{HEIGHT}")

canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()
# Variable that holds a ship object
player = Ship()

gameOver = False
TICK = .001

for row in range(3):
    for col in range(6):
        invader = Invader(20 + col*SPACEBETWEEN, 20 + row*SPACEABOVE)



while not gameOver:
    tk.update()
    player.updateBullets()
    time.sleep(TICK)
