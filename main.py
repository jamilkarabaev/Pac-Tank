import pygame
import random
import time


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)
pygame.init()

size = (640, 800)
screen = pygame.display.set_mode(size)

sprites_group = pygame.sprite.Group()
pacman_group = pygame.sprite.Group()
ghosts_group = pygame.sprite.Group()
walls_group = pygame.sprite.Group()
powerups_group = pygame.sprite.Group()
pacdots_group = pygame.sprite.Group()
gun_power_up_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
speed_powerups_group = pygame.sprite.Group()

pacman_image = pygame.image.load('pac-png.png')
cells = pygame.image.load('cells.png')
speed_power_up_image = pygame.image.load('speed_power_up_1.png')
gun_power_up_image = pygame.image.load('gun_power_up_image.png')

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([4,4])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 4
    
    def update(self):
        self.rect.x += self.speed



class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pacman_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.health = 100
        self.score = 0
        self.damage = 100
        self.score = 0
        self.gun_power_up_consumed = False
        self.start_time_gun_powerup = None
        self.start_time_speed_powerup = None
        self.end_time = None
        self.speed_powerup_incrementer = 0

    def update(self):
        self.end_time= pygame.time.get_ticks()
        if self.start_time_gun_powerup is not None:
            seconds = (self.end_time - self.start_time_gun_powerup)/1000
            if seconds >= 5:
                self.gun_power_up_consumed = False
        if self.start_time_speed_powerup is not None:
            seconds = (self.end_time - self.start_time_speed_powerup)/1000
            if seconds >= 5:
                self.speed_powerup_incrementer = 0
        
        self.rect.x += self.speed_x + self.speed_powerup_incrementer
        self.collide_x(walls_group)
        self.rect.y += self.speed_y + self.speed_powerup_incrementer
        self.collide_y(walls_group)
        self.collision_check(pacdots_group)
        self.collision_check(gun_power_up_group)
        self.collision_check(speed_powerups_group)
        self.display_score()
        
    def collide_x(self, sprite_group):
        block_hit_list = pygame.sprite.spritecollide(self, sprite_group, False)
        for block in block_hit_list:
            if self.speed_x > 0:
                self.rect.right = block.rect.left
            elif self.speed_x < 0:
                self.rect.left = block.rect.right

    def collide_y(self, sprite_group):
        block_hit_list = pygame.sprite.spritecollide(self, sprite_group, False)
        for block in block_hit_list:
            if self.speed_y > 0:
                self.rect.bottom = block.rect.top
            elif self.speed_y < 0:
                self.rect.top = block.rect.bottom


    def collision_check(self, group_type):
        block_hit_list = pygame.sprite.spritecollide(self, group_type, False)
        if block_hit_list:
            if group_type == gun_power_up_group:
                self.gun_power_up_consumed = True
                self.start_time_gun_powerup = pygame.time.get_ticks()
            if group_type == pacdots_group:
                self.score += 1
            if group_type == speed_powerups_group:
                self.speed_powerup_incrementer  = 10
                self.gun_power_up_consumed = True
                self.start_speed_powerup = pygame.time.get_ticks()
        for block in block_hit_list:
            block.kill()


    def shoot_if_gun_powerup_consumed(self):
        if self.gun_power_up_consumed == True:
            self.create_bullet(self.rect.x, self.rect.y)
        
    def create_bullet(self, x, y):
        bullet = Bullet(x, y+15)
        bullet_group.add(bullet)
            
        

    def display_score(self):
        font = pygame.font.SysFont("serif", 25)
        score = font.render("score: " + str(self.score), True, BLACK)
        screen.blit(score, [10, 650])
        if self.gun_power_up_consumed:
            seconds = (self.end_time - self.start_time_gun_powerup)/1000
            score = font.render("time-remaining: " + str(5-seconds), True, BLACK)
            screen.blit(score, [10, 750])
    


player = Pacman(40,40)
pacman_group.add(player)
        
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40,40])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class GhostCageWall(Wall):
    def __init__(self, x, y):
        Wall.__init__(self, x, y)
        self.image.fill(BLUE)

class CageDoor(Wall):
    def __init__(self, x, y):
        Wall.__init__(self, x ,y)
        self.image = cells


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40,40])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.consumed = False

class SpeedPowerUp(PowerUp):
    def __init__(self, x, y):
        PowerUp.__init__(self, x, y)
        self.image = speed_power_up_image

# class InvisibilityPowerUp(PowerUp):
#     def __init__(self, x, y):
#         PowerUp.__init__(self, x, y)
#         self.image = 

class Bullets(PowerUp):
    def __init__(self, x, y):
        PowerUp.__init__(self, x, y) 
        self.image = gun_power_up_image

gun_power_up_sprite = Bullets(450,45)
gun_power_up_group.add(gun_power_up_sprite)


class PacDot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([8,8])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.score_increment_value = 1

    def remove_on_pickup(self):
        block_hit_list = pygame.sprite.spritecollide(self, pacman_group, False)
        if block_hit_list:
            self.kill()

    def update(self):
        self.remove_on_pickup()

class Fruit(PacDot):
    def __init__(self, x, y):
        PacDot.__init__(self, x, y)
        self.image = pygame.Surface([30,30])
        self.image.fill(RED)
        self.score_increment_value = 10

fruit_sprite = Fruit(400,45)
pacdots_group.add(fruit_sprite)




sample_pac_dot = PacDot(200,60)
sample_pac_dot1 = PacDot(220,60)
sample_pac_dot2 = PacDot(260,60)
pacdots_group.add(sample_pac_dot)
pacdots_group.add(sample_pac_dot1)
pacdots_group.add(sample_pac_dot2)


speed_obj = SpeedPowerUp(40,40)
speed_powerups_group.add(speed_obj)

        



Maps = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 2, 3, 3, 2, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 2, 0, 0, 2, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 2, 2, 2, 2, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

for y in range(len(Maps)):
    for x in range(len(Maps)+1):
        if Maps[y][x] == 1:
            wall = Wall(x*40, y*40)
            walls_group.add(wall)
        elif Maps[y][x] == 2:
            wall = GhostCageWall(x*40, y*40)
            walls_group.add(wall)
        elif Maps[y][x] == 3:
            wall = CageDoor(x*40, y*40)
            walls_group.add(wall)





done = False
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed_y = 0
                player.speed_x = -5
            elif event.key == pygame.K_RIGHT:
                player.speed_y = 0
                player.speed_x = 5
            elif event.key == pygame.K_UP:
                player.speed_x = 0
                player.speed_y = -5
            elif event.key == pygame.K_DOWN:
                player.speed_x = 0
                player.speed_y = 5
            elif event.key == pygame.K_SPACE:
                player.shoot_if_gun_powerup_consumed()
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
    
    screen.fill(WHITE)
    player.update()
    powerups_group.update()
    pacdots_group.update()
    sprites_group.draw(screen)
    walls_group.draw(screen)
    ghosts_group.draw(screen)
    powerups_group.draw(screen)
    pacman_group.draw(screen)  
    pacdots_group.draw(screen)
    speed_powerups_group.draw(screen)
    gun_power_up_group.draw(screen)
    bullet_group.draw(screen)
    bullet_group.update()





    pygame.display.flip()
    clock.tick(60)
pygame.quit()