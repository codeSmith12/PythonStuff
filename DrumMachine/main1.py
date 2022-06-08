import pygame
from pygame import mixer
pygame.init()

WIDTH = 1400
HEIGHT = 800
BOTTOMBOXHEIGHT = 200
LEFTBOXWIDTH = 200
BORDERWIDTH = 5

black = (0,0,0)
white = (255,255,255)
gray = (128,128,128)

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Beat Maker')
labelFont = pygame.font.Font(None, 32)

FPS =  60 # Keep at 60
timer = pygame.time.Clock()


def drawGrid():
    leftBox = pygame.draw.rect(screen, gray, [0,0,LEFTBOXWIDTH, HEIGHT-BOTTOMBOXHEIGHT], BORDERWIDTH)
    bottomBox = pygame.draw.rect(screen, gray, [0,HEIGHT-BOTTOMBOXHEIGHT,WIDTH, BOTTOMBOXHEIGHT], BORDERWIDTH)




run = True
while run:
    timer.tick(FPS)
    screen.fill(black)
    drawGrid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip() # Place everything on the screen

pygame.quit()
