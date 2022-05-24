from tkinter import *
import time

class Invader:
    def __init__(self, x, y):
        self.x = x
        self.y = y



class Bullet:
    def __init__(self, pos):
        self.hit = False
        self.id = canvas.create_rectangle(pos[4]-SHIPSIZE//10,pos[1]-SHIPSIZE//2, pos[4]+SHIPSIZE//10, pos[5], fill=BULLETCOLOR, outline="")

class Ship:
    def __init__(self):
        self.id = canvas.create_polygon(WIDTH//2-SHIPSIZE//2, HEIGHT*7//8, WIDTH//2 + SHIPSIZE//2, HEIGHT*7//8, WIDTH//2, HEIGHT*7//8-SHIPSIZE, fill="lime")
        self.bullets = []
        tk.bind("<KeyPress-Left>", self.moveLeft)
        tk.bind("<KeyPress-Right>", self.moveRight)
        tk.bind("<space>", self.shoot)

    def moveLeft(self, event):
        canvas.move(self.id, -SHIPSPEED, 0)

    def moveRight(self,event):
        canvas.move(self.id, SHIPSPEED, 0)

    def shoot(self, event):
        pos = canvas.coords(self.id)
        bullet = Bullet(pos)
        self.bullets.append(bullet)

    def updateBullets(self):
        for bullet in self.bullets:
            canvas.move(bullet.id, 0, -10)





# Dimensions of space invader are square
WIDTH=600
HEIGHT=WIDTH
SHIPSIZE = 25
SHIPSPEED = 10
BULLETCOLOR="lime"

tk = Tk()
tk.title("Space Invader")
tk.geometry(f"{WIDTH}x{HEIGHT}")

canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()
# Variable that holds a ship object
player = Ship()

gameOver = False
TICK = .001

while not gameOver:
    tk.update()
    player.updateBullets()
    time.sleep(TICK)
