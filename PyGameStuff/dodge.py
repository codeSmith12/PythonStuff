import pygame
from random import randint
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("Ship.png").convert()
        self.surf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.surf.get_rect()
    def update(self, keys):
        if keys[K_UP]:
            self.rect.move_ip(0,-5)
        if keys[K_DOWN]:
            self.rect.move_ip(0,5)
        if keys[K_RIGHT]:
            self.rect.move_ip(5,0)
        if keys[K_LEFT]:
            self.rect.move_ip(-5,0)
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 500)


player = Player()

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

clock = pygame.time.Clock()


running = True

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    keysPressed = pygame.key.get_pressed()
    player.update(keysPressed)
    enemies.update()
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        running=False
    pygame.display.flip()
    clock.tick(30)
