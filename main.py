import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
pygame.init()

size = (600, 800)
screen = pygame.display.set_mode(size)

sprites_group = pygame.sprite.Group()
pacman_group = pygame.sprite.Group()
ghosts_group = pygame.sprite.Group()
walls_group = pygame.sprite.Group()
powerups_group = pygame.sprite.Group()

class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40,40])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.health = 100
        self.score = 0
        self.damage = 100

    def update(self):
        self.rect.x += self.speed_x
        self.collide_x(walls_group)
        self.rect.y += self.speed_y


    def collide_x(self, sprite_group):
        block_hit_list = pygame.sprite.spritecollide(self, sprite_group, False)
        for block in block_hit_list:
            if self.speed_x > 0:
                self.rect.right = block.rect.left
            elif self.speed_x < 0:
                self.rect.left = block.rect.right

player = Pacman(0,0)
pacman_group.add(player)
        
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40,40])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



Maps = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

for y in range(len(Maps)):
    for x in range(len(Maps)):
        if Maps[y][x] == 1:
            wall = Wall(x*40, y*40)
            walls_group.add(wall)






done = False
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed_x = -5
            elif event.key == pygame.K_RIGHT:
                player.speed_x = 5
            elif event.key == pygame.K_UP:
                player.speed_y = -5
            elif event.key == pygame.K_DOWN:
                player.speed_y = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.speed_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.speed_y = 0

    player.update() 
    
    screen.fill(WHITE)
    sprites_group.draw(screen)
    walls_group.draw(screen)
    ghosts_group.draw(screen)
    powerups_group.draw(screen)
    pacman_group.draw(screen)  





    pygame.display.flip()
    clock.tick(60)
pygame.quit()