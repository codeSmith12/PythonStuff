import pygame
from pygame import mixer


def drawGrid():
    leftBox = pygame.draw.rect(screen, gray, [0, 0, LEFTBOXWIDTH, HEIGHT-BOTTOMSIZE], BORDERWIDTH)
    bottomBox = pygame.draw.rect(screen, gray, [0, HEIGHT-BOTTOMSIZE, WIDTH, BOTTOMSIZE], BORDERWIDTH)
    boxes = []
    colors = [gray, white, gray]

    hiHatText = labelFont.render("Hi Hat", True, white)
    screen.blit(hiHatText, (LEFTBOXWIDTH/3,HEIGHT/12))
    snareText = labelFont.render("Snare", True, white)
    screen.blit(snareText, (LEFTBOXWIDTH/3,HEIGHT*2/12))
    kickText = labelFont.render("Kick", True, white)
    screen.blit(kickText, (LEFTBOXWIDTH/3,HEIGHT*3/12))



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

run = True

while run:
    timer.tick(FPS)
    screen.fill(black)
    drawGrid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
