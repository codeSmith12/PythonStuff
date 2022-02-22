import pygame, sys, time, random
# TUTORIAL FOLLOWED TO CREATE THIS:
# https://www.youtube.com/watch?v=UZg49z76cLw

# Once the second floor object hits x = 0, reset positions
def drawFloor():
    screen.blit(floor_surface,(floorX, 900))
    screen.blit(floor_surface,(floorX + width, 900)) # second floor object to scroll

# Creates a new pipe and returns it, type == rect
def createPipe():
    randomPipePos = random.choice(pipe_height)
    botPipe = pipeSurface.get_rect(midtop=(width+100, randomPipePos))
    topPipe = pipeSurface.get_rect(midbottom=(width+100, randomPipePos-300))
    return botPipe, topPipe

# Moves pipes of course...
def movePipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def drawPipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= height:
            # If bottom >= height, then this is the bottom pipe, and draw normally
            screen.blit(pipeSurface, pipe)
        else: # this is the top pipe, and we need to flip it vertically so its upsidedown
            flipPipe = pygame.transform.flip(pipeSurface, False, True)
            # Redraw this newly flipped pipe.
            screen.blit(flipPipe, pipe)

# Use pygames colliderect to check if two rectangles are touching, if they are, return false for some reason...
def checkCollision(pipes):
    for pipe in pipes:
        if birdRect.colliderect(pipe):
            deathSound.play()
            return False
    if birdRect.top <= -100 or birdRect.bottom >= 900:
        deathSound.play()
        return False

    return True

# Function to rotate bird upon flapping
def rotateBird(bird):
    newBird = pygame.transform.rotozoom(bird,birdMovement*-3, 1)
    return newBird

def birdAnimation():
    newBird = birdFrames[birdIndex]
    newBirdRect = newBird.get_rect(center = (100, birdRect.centery))
    return newBird, newBirdRect

# Depending on input, draw the score surfaces in particular ways
def scoreDisplay(gameState):
    if gameState == "mainGame":
        scoreSurface = gameFont.render(str(int(score)),True, (255,255,255))
        scoreRect = scoreSurface.get_rect(center=(width/2, 50))
        screen.blit(scoreSurface, scoreRect)

    if gameState == "gameOver":
        scoreSurface = gameFont.render(f"Score: {str(int(score))}",True, (255,255,255))
        scoreRect = scoreSurface.get_rect(center=(width/2, 50))
        screen.blit(scoreSurface, scoreRect)
        highScoreSurface = gameFont.render(f"High Score: {str(int(score))}",True, (255,255,255))
        highScoreRect = highScoreSurface.get_rect(center=(width/2, 850))
        screen.blit(highScoreSurface, highScoreRect)

# Used to set the highest score of all the runs (Resets upon exiting program.)
def update_score(score, highScore):
    if score > highScore:
        highScore = score
    return highScore


# Initialize mixer so audio isn't delayed. I commented out because it made popping sounds
# pygame.mixer.pre_init(frequency = 44100, size = 16, channels =1, buffer = 512)


pygame.init()



# Screen dimensions
width = 576 # Values should remain the same so images fit perfectly
height = 1024 # Values should remain the same so images fit perfectly
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

# Font stuff
gameFont = pygame.font.Font("04B_19.ttf",40)


# Game Variables
gravity = 0.20
birdMovement = 0
score = 0
highScore = 0


# Create a surface and load the background image into it, convert makes things faster
bg_surface = pygame.image.load("assets/background-day.png").convert()
# Double the size of the image to fit our screen.
bg_surface = pygame.transform.scale2x(bg_surface)

# Create surface for the floor, this will be object to detect if bird hits floor.
floor_surface = pygame.image.load("assets/base.png").convert()
# Double size of image to fit our screen
floor_surface = pygame.transform.scale2x(floor_surface)

# Variable to keep track of floors X value, used to slide image to make motion
floorX = 0

# These are different surfaces for each stage of the flap animation
birdDownFlap = pygame.transform.scale2x(pygame.image.load("assets/bluebird-downflap.png").convert_alpha())
birdMidFlap = pygame.transform.scale2x(pygame.image.load("assets/bluebird-midflap.png").convert_alpha())
birdUpFlap = pygame.transform.scale2x(pygame.image.load("assets/bluebird-upflap.png").convert_alpha())
# Put them all in a list to cycle through for animation
birdFrames = [birdDownFlap, birdMidFlap, birdUpFlap]

# Keeps track of the current bird image we are using
birdIndex = 0
# Use the same name to reduce refactoring
birdSurface = birdFrames[birdIndex]
birdRect = birdSurface.get_rect(center = (100, height/2))

BIRDFLAP = pygame.USEREVENT + 1 # + 1 because we can't use the same event number as the first event
pygame.time.set_timer(BIRDFLAP, 200)


# # Add an image for the bird, convert alpha will remove the black box around the rotating bird
# birdSurface = pygame.image.load("assets/bluebird-midflap.png").convert_alpha()
# # Double it's size
# birdSurface = pygame.transform.scale2x(birdSurface)
# # Place a rectangle around the bird image for collision detection and ability to rotate
# birdRect = birdSurface.get_rect(center = (100,height/2))

# Pipes are several rectangles that are sent across the screen with the same image
pipeSurface = pygame.image.load("assets/pipe-green.png").convert()
pipeSurface = pygame.transform.scale2x(pipeSurface)

# Contains every pipe in the game to loop over
pipeList = []

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200) # Call SPAWNPIPE event every 1.2 seconds

pipe_height = [400, 600, 800]

# Surface that holds game over image from the image assets folder
gameOverSurface = pygame.image.load("assets/message.png").convert_alpha()
gameOverSurface = pygame.transform.scale2x(gameOverSurface)
# Add rectangle to draw the surface onto for control of location
gameOverRect = gameOverSurface.get_rect(center = (width/2, height/2))

# 3 Sounds, one for flap, one for death and one for every 5 scores
flapSound = pygame.mixer.Sound("sound/sfx_wing.wav")
deathSound = pygame.mixer.Sound("sound/sfx_hit.wav")
scoreSound = pygame.mixer.Sound("sound/sfx_point.wav")
# Every 5 seconds, we will play the sound
scoreSoundCountdown = 500

# Is game currently running?
running = True
# Exits when someone hits X in corner
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # If the game is running and SPACE is hit, flap
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and running:
                birdMovement = 0
                birdMovement -= 8
                flapSound.play()

            # If game is not running and SPACE is hit, restart the game
            if event.key == pygame.K_SPACE and not running:
                running = True
                pipeList.clear() # Remove all pipes from list upon restart
                birdRect.center= (100, height/2) # reset birds location
                birdMovement = 0 # Make sure bird gravity isnt carried over from last game
                score = 0
        # Used to decide which bird image to use during flap animation
        if event.type == BIRDFLAP:
            if birdIndex < 2:
                birdIndex += 1
            else:
                birdIndex = 0
            birdSurface, birdRect = birdAnimation()

        # Using user created event, spawn a pipe every 1.2 seconds
        if event.type == SPAWNPIPE:
            pipeList.extend(createPipe()) # Returns a tuple, so we had to use extend

    screen.blit(bg_surface, (0,0)) # puts one surface onto another

    # If the game is active
    if running:
        # Bird logic
        birdMovement += gravity
        rotatedBird = rotateBird(birdSurface)
        birdRect.centery += birdMovement
        screen.blit(rotatedBird, birdRect)
        running = checkCollision(pipeList)
        # Pipes logic
        pipeList = movePipes(pipeList)
        drawPipes(pipeList)

        # Score logic
        score += .01
        scoreSoundCountdown -=1
        if scoreSoundCountdown <= 0:
            scoreSound.play()
            scoreSoundCountdown = 500
        scoreDisplay("mainGame") # Display the score while game is running
    else: # after the user has died, display high score
        screen.blit(gameOverSurface, gameOverRect)
        highScore = update_score(score, highScore)
        scoreDisplay("gameOver")


    # Floor logic
    floorX -= 1
    drawFloor()
    if floorX <= -width:
        floorX = 0
    screen.blit(floor_surface, (floorX,900)) # puts one surface onto another


    # Update all of the changes we made to surface locations
    pygame.display.update()
    # Our game can have up to 120 FPS, but may also have lower depending on hardware
    clock.tick(120)
