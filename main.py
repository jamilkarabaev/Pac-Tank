import pygame
import random
import time

Map1 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 2, 0, 0, 2, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 2, 2, 2, 2, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

Map2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 2, 0, 0, 2, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 2, 2, 2, 2, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
Map3 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 2, 0, 0, 2, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 2, 2, 2, 2, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
Map4 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 2, 0, 0, 2, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 2, 2, 2, 2, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
Map5 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 2, 0, 0, 2, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 2, 2, 2, 2, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)
pygame.init()

font_path = r"joystix_monospace.ttf"
font = pygame.font.Font(font_path, 20)

size = (640, 800)
screen = pygame.display.set_mode(size)


buttons_group = pygame.sprite.Group()
sprites_group = pygame.sprite.Group()
pactank_group = pygame.sprite.Group()
ghosts_group = pygame.sprite.Group()
walls_group = pygame.sprite.Group()
powerup_group = pygame.sprite.Group()
pacdots_group = pygame.sprite.Group()
fruits_group = pygame.sprite.Group()
bullets_powerup_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
speed_powerup_group = pygame.sprite.Group()
invisibility_powerup_group = pygame.sprite.Group()
powerpellet_powerup_group = pygame.sprite.Group()


green_tank_right_sprite = pygame.image.load('sprites\green_tank_right_sprite.png')
green_tank_down_sprite = pygame.image.load('sprites\green_tank_down_sprite.png')
green_tank_left_sprite = pygame.image.load('sprites\green_tank_left_sprite.png')
green_tank_up_sprite = pygame.image.load('sprites\green_tank_up_sprite.png')
blinky_sprite = pygame.image.load('sprites\_red_ghost_sprite.png')
pinky_sprite = pygame.image.load('sprites\pink_ghost_sprite.png')
inky_sprite = pygame.image.load('sprites\_blue_ghost_sprite.png')
clyde_sprite = pygame.image.load('sprites\orange_ghost_sprite.png')
speed_powerup_sprite = pygame.image.load('sprites\speed_powerup_sprite.png')
bullets_powerup_sprite = pygame.image.load('sprites\_bullets_powerup_sprite.png')
single_bullet_sprite = pygame.image.load('sprites\single_bullet_sprite.png')
invisibility_powerup_sprite = pygame.image.load('sprites\invisibility_powerup_sprite.png')
redbrick_wall_sprite = pygame.image.load('sprites\_redbrick_wall_sprite.png')


class Button():
    def __init__(self, x, y, color, width, height, text):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.text = text

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)
        text = font.render(self.text, True, BLACK)
        screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def mouse_is_over(self, pos):
        # where pos is a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False



class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = single_bullet_sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.direction = direction
        self.speed_variable_constructor()

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.collision_check(walls_group)

    def speed_variable_constructor(self):
        if self.direction == 'right': 
            self.speed_x = 20
            self.speed_y = 0
        elif self.direction == 'left':
            self.speed_x = -20
            self.speed_y = 0
        elif self.direction == 'down':
            self.speed_x = 0
            self.speed_y = 20
        elif self.direction == 'up':
            self.speed_x = 0
            self.speed_y = -20

    def collision_check(self, group_type):
        block_hit_list = pygame.sprite.spritecollide(self, group_type, False)
        if block_hit_list:
            if group_type == walls_group:
                self.kill()

class PacTank(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = [green_tank_right_sprite, green_tank_down_sprite, green_tank_left_sprite, green_tank_up_sprite]
        self.image_index = 0
        self.image = self.get_image()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.score = 0
        self.lives = 3
        self.level = 0
        self.end_time = None
        self.bullets_powerup_consumed = False
        self.start_time_bullets_powerup = None
        self.speed_powerup_incrementer = 0
        self.start_time_speed_powerup = None
        self.invisibility_powerup_consumed = False
        self.start_time_invisibility_powerup = None
        self.powerpellet_powerup_consumed = False
        self.start_time_powerpellet_powerup = None
        self.direction = 'right'
        self.respawn_needed = False

    def reset_main_variable(self):
        self.end_time = None
        self.bullets_powerup_consumed = False
        self.start_time_bullets_powerup = None
        self.speed_powerup_incrementer = 0
        self.start_time_speed_powerup = None
        self.invisibility_powerup_consumed = False
        self.start_time_invisibility_powerup = None
        self.powerpellet_powerup_consumed = False
        self.start_time_powerpellet_powerup = None

    def set_image(self, index):
        self.image_index = index

    def get_image(self):
        return self.images[self.image_index]

    def update(self):
        self.image = self.get_image()
        self.end_time= pygame.time.get_ticks()
        if self.start_time_bullets_powerup is not None:
            seconds = (self.end_time - self.start_time_bullets_powerup)/1000
            if seconds >= 5:
                self.bullets_powerup_consumed = False
        if self.start_time_speed_powerup is not None:
            seconds = (self.end_time - self.start_time_speed_powerup)/1000
            if seconds >= 5:
                self.speed_powerup_incrementer = 0
        if self.start_time_invisibility_powerup is not None:
            seconds = (self.end_time - self.start_time_invisibility_powerup)/1000
            if seconds >= 5:
                self.invisibility_powerup_consumed = False
        if self.start_time_powerpellet_powerup is not None:
            seconds = (self.end_time - self.start_time_powerpellet_powerup)/1000
            if seconds >= 5:
                self.powerpellet_powerup_consumed = False
        
        if self.speed_x == 5:
            self.set_image(0)
            self.direction = 'right'
            if self.speed_powerup_incrementer != 0:
                self.speed_x += self.speed_powerup_incrementer
        elif self.speed_y == 5:
            self.direction = 'down'
            self.set_image(1)
            if self.speed_powerup_incrementer != 0:
                self.speed_y += self.speed_powerup_incrementer
        elif self.speed_x == -5:
            self.direction = 'left'
            self.set_image(2)
            if self.speed_powerup_incrementer != 0:
                self.speed_x -= self.speed_powerup_incrementer
        elif self.speed_y == -5:
            self.direction = 'up'
            self.set_image(3)
            if self.speed_powerup_incrementer != 0:
                self.speed_y -= self.speed_powerup_incrementer
            
        self.rect.x += self.speed_x
        self.collide_x(walls_group)
        self.rect.y += self.speed_y
        self.collide_y(walls_group)
        self.collision_check(pacdots_group)
        self.collision_check(bullets_powerup_group)
        self.collision_check(speed_powerup_group)
        self.collision_check(invisibility_powerup_group)
        self.collision_check(fruits_group)
        self.display_score()
        self.check_collide_with_ghost()
        
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
            if group_type == bullets_powerup_group:
                self.bullets_powerup_consumed = True
                self.start_time_bullets_powerup = pygame.time.get_ticks()
            elif group_type == pacdots_group:
                self.score += 1
            elif group_type == fruits_group:
                self.score += 5
            elif group_type == speed_powerup_group:
                self.speed_powerup_incrementer = 7
                self.start_time_speed_powerup = pygame.time.get_ticks()
            elif group_type == invisibility_powerup_group:
                self.invisibility_powerup_consumed = True
                self.start_time_invisibility_powerup = pygame.time.get_ticks()
            elif group_type == powerpellet_powerup_group:
                self.powerpellet_powerup_consumed = True
                self.start_time_powerpellet_powerup = pygame.time.get_ticks()
        for block in block_hit_list:
            block.kill()

    def check_collide_with_ghost(self):
        block_hit_list = pygame.sprite.spritecollide(self, ghosts_group, False)
        if block_hit_list:
            self.lives -= 1
            self.respawn_needed = True



    def shoot_if_bullets_powerup_consumed(self):
        if self.bullets_powerup_consumed == True:  
            bullet = Bullet(self.rect.x + 18, self.rect.y + 18, self.direction)
            bullet_group.add(bullet)

    def display_score(self):

        lives = font.render("lives:" + str(self.lives), True, BLACK)
        screen.blit(lives, [10, 600])
        score = font.render("score:" + str(self.score), True, BLACK)
        screen.blit(score, [150, 600])
        score = font.render("level:" + str(self.level), True, BLACK)
        screen.blit(score, [290 , 600])
        if self.speed_powerup_incrementer:
            seconds = (self.end_time - self.start_time_speed_powerup)/1000
            speed_powerup_timer = font.render("speed powerup timer: " + str(int(5-seconds)), True, BLACK)
            screen.blit(speed_powerup_timer, [10, 670])   
        if self.bullets_powerup_consumed:
            seconds = (self.end_time - self.start_time_bullets_powerup)/1000
            bullets_powerup_timer = font.render("bullets powerup timer: " + str(int(5-seconds)), True, BLACK)
            screen.blit(bullets_powerup_timer, [10, 700])
        if self.invisibility_powerup_consumed:
            seconds = (self.end_time - self.start_time_invisibility_powerup)/1000
            invisibility_powerup_timer = font.render("invisibility powerup timer: " + str(int(5-seconds)), True, BLACK)
            screen.blit(invisibility_powerup_timer, [10, 730])

    def four_steps_ahead(self):
        if self.direction == 'right':
            return int((self.rect.x + 4*40)/40), int((self.rect.y)/40)
        elif self.direction == 'left':
            return int((self.rect.x - 4*40)/40),int((self.rect.y)/40)
        elif self.direction == 'up':
            return int((self.rect.x)/40), int((self.rect.y - 4*40)/40)
        elif self.direction == 'down':
            return int((self.rect.x)/40), int((self.rect.y + 4*40)/40)







     
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = redbrick_wall_sprite
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class GhostCageWall(Wall):
    def __init__(self, x, y):
        Wall.__init__(self, x, y)

class CageDoor(Wall):
    def __init__(self, x, y):
        Wall.__init__(self, x ,y)
        self.image.fill(RED)

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
        self.image = speed_powerup_sprite

class Bullets(PowerUp):
    def __init__(self, x, y):
        PowerUp.__init__(self, x, y) 
        self.image = bullets_powerup_sprite

class InvisibilityPowerUp(PowerUp):
    def __init__(self, x, y):
        PowerUp.__init__(self, x, y)
        self.image = invisibility_powerup_sprite

class PowerPellet(PowerUp):
    def __init__(self, x, y):
        PowerUp.__init__(self, x, y)
        self.image = pygame.Surface([30,30])
        self.image.fill(YELLOW)

class PacDot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([8,8])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.score_increment_value = 1 

class Fruit(PacDot):
    def __init__(self, x, y):
        PacDot.__init__(self, x, y)
        self.image = pygame.Surface([30,30])
        self.image.fill(RED)



player = PacTank(40,40)
pactank_group.add(player)

class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, map, type):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        if self.type == 'blinky':
            self.image = blinky_sprite
        elif self.type == 'pinky':
            self.image = pinky_sprite
        elif self.type == 'inky':
            self.image = inky_sprite
        elif self.type == 'clyde':
            self.image = clyde_sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.grid_x = int(self.rect.x/40)
        self.grid_y = int(self.rect.y/40)
        self.speed_x = 5
        self.speed_y = 5
        self.map = map
        self.execute_bfs = True
        self.incrementation_amounts = []
        self.counter = 0


    def update(self):
        self.move()
        self.check_for_bullet_collision()

    def check_for_bullet_collision(self):
        block_hit_list = pygame.sprite.spritecollide(self, bullet_group, False)
        if block_hit_list:
            for block in block_hit_list:
                block.kill()
            self.kill()


    def move(self):
        if self.type == 'blinky':
            self.move_shortest_path(4)
        elif self.type == 'pinky':
            self.move_shortest_path(5)
        elif self.type == 'inky':
            self.move_shortest_path(5)
        elif self.type == 'clyde':
            self.move_shortest_path(5)

    def target_four_steps_ahead(self, map):
        spot_x, spot_y = player.four_steps_ahead()
        if spot_x >= 0 and spot_x <= 15 and spot_y >= 0 and spot_y <= len(map)-1:
            if map[spot_y][spot_x] != 1 and map[spot_y][spot_x] != 2 and map[spot_y][spot_x] != 3:
                return [spot_x, spot_y]
            else:
                return [int(player.rect.x/40), int(player.rect.y/40)]
        else:
            return [int(player.rect.x / 40), int(player.rect.y / 40)]



    def move_shortest_path(self, incrementation_rate):
        if self.execute_bfs:
            self.incrementation_amounts = self.attain_movement()
            if self.incrementation_amounts == None:
                return
            else:
                self.execute_bfs = False
        else:
            self.counter += incrementation_rate

            x_increment, y_increment = self.incrementation_amounts


            if x_increment > 0:
                self.rect.x +=incrementation_rate
            elif x_increment < 0:
                self.rect.x -=incrementation_rate
            elif y_increment > 0:
                self.rect.y +=incrementation_rate
            elif y_increment < 0:
                self.rect.y -=incrementation_rate

            if self.counter >= 40:
                self.execute_bfs = True
                self.counter = 0
            

            
        


    
    def attain_movement(self):
        if player.invisibility_powerup_consumed == True:
            next_cell = self.find_random_cell()
        else:
            if self.type == 'clyde':
                next_cell = self.find_random_cell()
            else:
                next_cell = self.find_next_cell_in_path()

        if next_cell != None:
            x_increment = next_cell[0] - self.rect.x/40
            y_increment = next_cell[1] - self.rect.y/40
            return x_increment, y_increment
        else:
            return None

    def find_random_cell(self):
        while True:
            number = random.randint(-2, 1)
            if number == -2:
                x_addition, y_addition = 1, 0
            elif number == -1:
                x_addition, y_addition = 0, 1
            elif number == 0:
                x_addition, y_addition = -1, 0
            elif number == 1:
                x_addition, y_addition = 0, -1
            if self.map[int(self.rect.y/40) + y_addition][int(self.rect.x/40) + x_addition] != 1 and self.map[int(self.rect.y/40) + y_addition][int(self.rect.x/40) + x_addition] != 2 and self.map[int(self.rect.y/40) + y_addition][int(self.rect.x/40) + x_addition] != 3:
                return[int(self.rect.x/40) + x_addition, int(self.rect.y/40) + y_addition]



    def find_next_cell_in_path(self):
        if self.type == 'inky':
            path = self.bfs([int(self.rect.x/40), int(self.rect.y/40)], self.target_four_steps_ahead(self.map))
        else:
            path = self.bfs([int(self.rect.x/40), int(self.rect.y/40)], [int(player.rect.x/40), int(player.rect.y/40)])
        if len(path) > 1:
            return path[1]
        else:
            return None
    
    def bfs(self, start, target):

        grid = self.map
        queue = [start]
        path = []
        visited = []

        while queue:
            current = queue[0]
            queue.remove(queue[0])
            visited.append(current)

            if current == target:
                break
            else:
                neighbours = [[0, -1], [1, 0], [0, 1], [-1, 0]]
                for neighbour in neighbours:
                    if neighbour[0]+current[0] >= 0 and neighbour[0] + current[0] < len(grid[0]):
                        if neighbour[1]+current[1] >= 0 and neighbour[1] + current[1] < len(grid):
                            next_cell = [neighbour[0] + current[0], neighbour[1] + current[1]]
                            if next_cell not in visited:
                                if grid[next_cell[1]][next_cell[0]] != 1 and grid[next_cell[1]][next_cell[0]]!= 2 and grid[next_cell[1]][next_cell[0]]!=3:
                                    queue.append(next_cell)
                                    path.append({"Current": current, "Next": next_cell})


        shortest = [target]
        while target != start:
            for step in path:
                if step["Next"] == target:
                    target = step["Current"]
                    shortest.insert(0, step["Current"])
        return shortest








def generate_list_of_non_wall_coords(map):
    y_coords = []
    x_coords = []
    List_of_non_wall_coords = []
    for y in range(len(map)):
        for x in range(len(map)+1):
            if map[y][x] != 1 and map[y][x] != 2 and map[y][x] != 3:
                List_of_non_wall_coords.append([y,x])
    return List_of_non_wall_coords

def check_for_valid_move(move_direction, map):
    List_of_non_wall_coords = generate_list_of_non_wall_coords(map)
    

    player_x = player.rect.x/40
    player_x_right = player_x + 1
    player_x_left = player_x - 1

    player_y = player.rect.y/40
    player_y_down = player_y + 1
    player_y_up = player_y - 1

    if move_direction == 'right':
        if [player_y, player_x_right] in List_of_non_wall_coords:
            return True
    elif move_direction == 'left':
        if [player_y, player_x_left] in List_of_non_wall_coords:
            return True
    elif move_direction == 'down':
        if [player_y_down, player_x] in List_of_non_wall_coords:
            return True
    elif move_direction == 'up':
        if [player_y_up, player_x] in List_of_non_wall_coords:
            return True
    else:
        return False

def generate_free_coords(map):
    List_of_free_spots = []
    for y in range(len(map)):
        for x in range(len(map)+1):
            if map[y][x] == 0:
                List_of_free_spots.append([y,x])
    current_range = len(List_of_free_spots) - 1
    picked_index = random.randrange(0, current_range, 1)
    picked_coordinates = List_of_free_spots[picked_index]
    return picked_coordinates

def list_of_all_remaining_free_coords(map):
    List_of_free_spots = []
    for y in range(len(map)):
        for x in range(len(map)+1):
            if map[y][x] == 0:
                List_of_free_spots.append([y,x])
    return List_of_free_spots

def take_spots(map, y, x):
    map[y][x] = 4
           
backgrounds = []

def start_level(level, current_map):
    for ghost in ghosts_group:
        ghost.kill()


    ghosts_group.empty()
    walls_group.empty()
    powerup_group.empty()
    pacdots_group.empty()
    fruits_group.empty()
    bullets_powerup_group.empty()
    bullet_group.empty()
    speed_powerup_group.empty()
    invisibility_powerup_group.empty()
    powerpellet_powerup_group.empty()

    player.reset_main_variable()


    for y in range(len(current_map)):
        for x in range(len(current_map)+1):
            if current_map[y][x] == 1:
                wall = Wall(x*40, y*40)
                walls_group.add(wall)
            elif current_map[y][x] == 2:
                wall = GhostCageWall(x*40, y*40)
                walls_group.add(wall)
            elif current_map[y][x] == 3:
                wall = CageDoor(x*40, y*40)
                walls_group.add(wall)


    #placing the objects in the map
    player.rect.x = 40
    player.rect.y = 40
    starting_player_position = [1,1]
    take_spots(current_map, starting_player_position[0], starting_player_position[1])

    pinky = Ghost(7 * 40, 7 * 40, current_map, 'pinky')
    blinky = Ghost(8*40, 7*40, current_map, 'blinky')
    inky = Ghost(7*40, 8*40, current_map, 'inky')
    clyde = Ghost(8*40, 8*40, current_map, 'clyde')
    ghosts_group.add(blinky)
    ghosts_group.add(pinky)
    ghosts_group.add(inky)
    ghosts_group.add(clyde)
    take_spots(current_map, 7, 7)
    take_spots(current_map, 7, 8)
    take_spots(current_map, 8, 7)
    take_spots(current_map, 8, 8)


    for i in range(level+5):
        frequency_decider = random.randrange(0, 11, 1)
        if frequency_decider < 8:
            position_for_item = generate_free_coords(current_map)
            type_decider = random.randrange(0, 5, 1)
            if type_decider == 0:
                bullets_powerup_obj = Bullets(position_for_item[1]*40,position_for_item[0]*40)
                bullets_powerup_group.add(bullets_powerup_obj)
            elif type_decider == 1:
                speed_powerup_obj = SpeedPowerUp(position_for_item[1]*40,position_for_item[0]*40)
                speed_powerup_group.add(speed_powerup_obj)
            elif type_decider == 2:
                invisibility_powerup_obj = InvisibilityPowerUp(position_for_item[1]*40,position_for_item[0]*40)
                invisibility_powerup_group.add(invisibility_powerup_obj)
            elif type_decider == 3:
                powerpellet_powerup_obj = PowerPellet(position_for_item[1]*40+5,position_for_item[0]*40+5)
                powerpellet_powerup_group.add(powerpellet_powerup_obj)
            elif type_decider == 4:
                fruit_obj = Fruit(position_for_item[1]*40+5,position_for_item[0]*40+5)
                fruits_group.add(fruit_obj)
            take_spots(current_map, position_for_item[0], position_for_item[1])

    remaining_free_positions = list_of_all_remaining_free_coords(current_map)
    for position in remaining_free_positions:
        pacdot = PacDot(position[1]*40+16, position[0]*40+16)
        pacdots_group.add(pacdot)
        take_spots(current_map, position[0], position[1])
    
    









def generate_new_map(level):
    if level == 1:
        current_map = Map1
    elif level == 2:
        current_map = Map2
    elif level == 3:
        current_map = Map3
    elif level == 4:
        current_map = Map4
    elif level == 5:
        current_map = Map5
    return current_map


def check_for_queues():
    if queued_move == 'left':
        if check_for_valid_move('left', current_map) == True:
            player.speed_y = 0
            player.speed_x = -5
    elif queued_move == 'right':
        if check_for_valid_move('right', current_map) == True:
            player.speed_y = 0
            player.speed_x = 5
    elif queued_move == 'up':
        if check_for_valid_move('up', current_map) == True:
            player.speed_y = -5
            player.speed_x = 0
    elif queued_move == 'down':
        if check_for_valid_move('down', current_map) == True:
            player.speed_y = 5
            player.speed_x = 0




done = False
clock = pygame.time.Clock()
level = 0
queued_move = None
start_time = pygame.time.get_ticks()
game_start = False
map_copy = None






while not done:
    if game_start == False:
        screen.fill(BLACK)

        play_button = Button(160, 200, GREEN, 300, 100,  'PLAY')
        play_button.draw()

        instructions_button = Button(160, 400, GREEN, 300, 100, 'INSTRUCTIONS')
        instructions_button.draw()

        cosmetics_button = Button(160, 600, GREEN, 300, 100, 'COSMETICS')
        cosmetics_button.draw()

        pactank_text = font.render("PAC TANK", True, WHITE)
        screen.blit(pactank_text, (240,80))

        for event in pygame.event.get():
            mouse_pointer = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.mouse_is_over(mouse_pointer):
                    game_start = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
    else:
        if player.level == 5:
            done = True
        if len(pacdots_group) == 0:
            player.level+=1
            player.respawn_needed = False
            current_map = generate_new_map(player.level)
            map_copy = list(current_map)
            print(map_copy)
            start_level(player.level, current_map)
            if current_map == map_copy:
                print("unfortunately they are equal")
            print(map_copy)
        elif player.respawn_needed:
            player.respawn_needed = False
            current_map = map_copy.copy()
            print(map_copy.copy())
            start_level(player.level, current_map)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    queued_move = None
                    if check_for_valid_move('left', current_map) == True:
                        player.speed_y = 0
                        player.speed_x = -5
                    else:
                        queued_move = 'left'
                elif event.key == pygame.K_RIGHT:

                    queued_move = None
                    if check_for_valid_move('right', current_map) == True:
                        player.speed_y = 0
                        player.speed_x = 5
                    else:
                        queued_move = 'right'
                elif event.key == pygame.K_UP:
                    queued_move = None
                    if check_for_valid_move('up', current_map) == True:
                        player.speed_x = 0
                        player.speed_y = -5
                    else:
                        queued_move = 'up'
                elif event.key == pygame.K_DOWN:
                    queued_move = None
                    if check_for_valid_move('down', current_map) == True:
                        player.speed_x = 0
                        player.speed_y = 5
                    else:
                        queued_move = 'down'
                elif event.key == pygame.K_SPACE:
                    player.shoot_if_bullets_powerup_consumed()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()

        check_for_queues()

        screen.fill(WHITE)
        sprites_group.draw(screen)
        walls_group.draw(screen)
        ghosts_group.draw(screen)
        powerup_group.draw(screen)
        bullet_group.draw(screen)
        fruits_group.draw(screen)
        pactank_group.draw(screen)
        pacdots_group.draw(screen)

        speed_powerup_group.draw(screen)
        bullets_powerup_group.draw(screen)
        invisibility_powerup_group.draw(screen)

        ghosts_group.update()

        player.update()
        powerup_group.update()
        bullet_group.update()

    pygame.display.flip()
    clock.tick(60)
pygame.quit()