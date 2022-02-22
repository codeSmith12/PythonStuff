import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 165
fpsClock = pygame.time.Clock()



displaySurf = pygame.display.set_mode((1000,800), 0, 32)
pygame.display.set_caption("Dog Animation")

WHITE = (255,255,255)
dogImg = pygame.image.load('courage.png')
dogX = 10
dogY = 10
direction = "right"
while True:
    displaySurf.fill(WHITE)
    if direction == "right":
        dogX += 5
        if dogX == 280:
            direction = "down"

    elif direction == "down":
        dogY += 5
        if dogY == 220:
            direction = "left"
    elif direction == "left":
        dogX -= 5
        if dogX == 10:
            direction = "up"
    elif direction == "up":
        dogY -= 5
        if dogY == 10:
            direction = "right"
    displaySurf.blit(dogImg, (dogX, dogY))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
