import pygame
from projectiles import ProjectileWarrior
import time

class Player1(pygame.sprite.Sprite):
    def __init__(self, classe):
        super().__init__()
        self.health = 100
        self.maxhealth = 100
        self.all_projectiles = pygame.sprite.Group()
        self.attack = 50
        self.velocity = 15

        self.isJump = False
        self.jumpEnd = time.time()


        self.image = pygame.image.load('assets/warrior/warrior.png')
        self.rect = self.image.get_rect()
        self.rect.y = 595




        self.attack1 = None
        if classe == "guerrier":
            self.attack1 = ProjectileWarrior
        self.attack1_cd = 1.5
        self.attack1_last_use = time.time() - 5

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.isJump = True
        self.jumpEnd = time.time() + 1



    def launch_projectile(self, dir):
        self.all_projectiles.add(self.attack1(self, dir))

class Player2(pygame.sprite.Sprite):
    def __init__(self, classe):
        super().__init__()
        self.health = 100
        self.maxhealth = 100
        self.all_projectiles = pygame.sprite.Group()
        self.attack = 50
        self.velocity = 20

        self.attack1 = None
        if classe == "guerrier":
            self.attack1 = ProjectileWarrior
        self.attack1_cd = 1.5
        self.attack1_last_use = time.time() - 5

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def launch_projectile(self, dir):
        self.all_projectiles.add(self.attack1(self, dir))