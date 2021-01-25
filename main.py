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
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.health = 100
        self.score = 0
        self.damage = 100
        
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image = pygame.Surface([40,40])
        self.image.fill(BLACK)
        
                