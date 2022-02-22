import pygame, sys
from pygame.locals import *
import time

pygame.init()
# soundObj = pygame.mixer.Sound("coin.wav")
# soundObj.play()
# time.sleep(1)
# soundObj.stop()

displaySurf = pygame.display.set_mode((400,300), 0, 32)
pygame.display.set_caption("Text Stuff")

WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)

fontObj = pygame.font.Font("freesansbold.ttf",32)
textSurfaceObj = fontObj.render("Hello world!", True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200,150)

while True:
    displaySurf.fill(WHITE)
    displaySurf.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
