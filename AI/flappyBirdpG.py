import pygame, time


gravity = 1


# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800,600))

# Set the title of the window
pygame.display.set_caption("Flappy Bird")
# Create an icon
icon = pygame.image.load('flappyBird.jpg')
# Set Icon
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('flappyBird.jpg')
global playerX
playerX = 150
global playerY
playerY = 300

def player():
    global playerY
    playerY = playerY + gravity
    screen.blit(playerImg, (playerX, playerY+gravity))
    time.sleep(.005)


# Game Loop
running = True
while running:
    screen.fill((0,200,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player()
    pygame.display.update()
