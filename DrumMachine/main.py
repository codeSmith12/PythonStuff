import pygame
from pygame import mixer


def drawGrid(clicked):
    leftBox = pygame.draw.rect(screen, gray, [0, 0, LEFTBOXWIDTH, HEIGHT-BOTTOMSIZE], BORDERWIDTH)
    bottomBox = pygame.draw.rect(screen, gray, [0, HEIGHT-BOTTOMSIZE, WIDTH, BOTTOMSIZE], BORDERWIDTH)
    boxes = []
    colors = [gray, white, gray]

    hiHatText = labelFont.render("Hi Hat", True, white)
    screen.blit(hiHatText, (LEFTBOXWIDTH/3,50))
    snareText = labelFont.render("Snare", True, white)
    screen.blit(snareText, (LEFTBOXWIDTH/3,150))
    kickText = labelFont.render("Kick", True, white)
    screen.blit(kickText, (LEFTBOXWIDTH/3,250))
    crashText = labelFont.render("Crash", True, white)
    screen.blit(crashText, (LEFTBOXWIDTH/3,350))
    clapText = labelFont.render("Clap", True, white)
    screen.blit(clapText, (LEFTBOXWIDTH/3,440))
    floorText = labelFont.render("Floor Tom", True, white)
    screen.blit(floorText, (LEFTBOXWIDTH/4,530))

    for i in range(1,instruments):
        pygame.draw.line(screen, gray, [0, i*100], (LEFTBOXWIDTH, i*100), 3)

    for i in range(beats):
        for j in range(instruments):
            rect = pygame.draw.rect(screen, gray, [i*((WIDTH-LEFTBOXWIDTH) // beats) + LEFTBOXWIDTH, (j*100), ((WIDTH-LEFTBOXWIDTH) // beats), ((HEIGHT-BOTTOMSIZE)//instruments)], 5, 5)
            boxes.append((rect, (i,j)))

    return boxes


pygame.init()

WIDTH = 1400
HEIGHT = 800
LEFTBOXWIDTH = 200
BORDERWIDTH = 5
BOTTOMSIZE = 200

black = (0,0,0)
white = (255,255,255)
gray = (128,128,128)

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Beat Maker")

labelFont = pygame.font.Font(None, 32)

FPS = 60
timer = pygame.time.Clock()
beats = 8
instruments = 6
boxes = []
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]

run = True

while run:
    timer.tick(FPS)
    screen.fill(black)
    boxes = drawGrid(clicked)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(boxes)):
                if boxes[i][0].colliderect(event.pos):
                    coords = boxes[i][1] # Grabs the tuple of x,y belonging to box
                    clicked[coords[1]][coords[0]] *= -1


    pygame.display.flip()

pygame.quit()
