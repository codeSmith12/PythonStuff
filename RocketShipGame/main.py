import pygame

class Ship:
    def __init__(self):
        self.size = SHIPSIZE
        self.yVel = 0
        self.boost = False
        self.pointLeft = [WIDTH//2-SHIPSIZE//2, HEIGHT//2]
        self.pointRight = [WIDTH//2+SHIPSIZE//2, HEIGHT//2]
        self.pointTop = [WIDTH//2, HEIGHT//2 - SHIPSIZE]
        self.id = pygame.draw.polygon(screen, "white",points=[self.pointLeft, self.pointTop, self.pointRight]) #pygame.Rect(WIDTH//2,HEIGHT//2,SHIPSIZE,SHIPSIZE)
        pygame.display.flip()

    def getPoints(self):
        return [self.pointLeft, self.pointTop, self.pointRight]
    def turnLeft(self):
        self.id = pygame.transform.rotate(self.id, 10)

    def updatePos(self):
        if self.boost:
            self.yVel -= .2
        if self.yVel < MAXFALLSPEED and not self.boost:
            self.yVel += .2
        self.pointLeft[1] += self.yVel
        self.pointRight[1] += self.yVel
        self.pointTop[1] += self.yVel
        self.id = pygame.draw.polygon(screen, "white",points=[self.pointLeft, self.pointTop, self.pointRight]) #pygame.Rect(WIDTH//2,HEIGHT//2,SHIPSIZE,SHIPSIZE)


pygame.init()

WIDTH = 1000
HEIGHT = 1000
SHIPSIZE = 20
GRAVITY = 1
MAXFALLSPEED = 6
MAXSPEED = 10
FPS=60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crash Landing")


ship = Ship()

running = True

tick = pygame.time.Clock()


while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ship.yVel -= 1
                ship.boost = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                ship.boost = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship.turnLeft()

    ship.updatePos()

    pygame.display.update()
    tick.tick(FPS)
