import pygame
from projectiles import ProjectileWarrior
import time
import animation

class Player1(animation.AnimateSprite):
    def __init__(self, classe, game):
        self.attack1 = None
        if classe == "guerrier":
            super().__init__("warrior")

            self.attack1 = ProjectileWarrior

        self.health = 100
        self.maxhealth = 100
        self.all_projectiles = pygame.sprite.Group()
        self.attack = 50
        self.velocity = 5
        self.isJump = False
        self.jumpEnd = time.time()
        self.game = game
        self.rect = self.image.get_rect()
        self.rect.y = 400



        self.attack1_cd = 1.5
        self.attack1_last_use = time.time() - 5

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.isJump = True
        self.jumpEnd = time.time() + 1

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount

    def update_health_bar(self, surface):
        pygame.draw.rect(surface,(60,63,60), [self.rect.x + 20, self.rect.y - 20, self.maxhealth, 5])
        pygame.draw.rect(surface,(111,210,46), [self.rect.x + 20, self.rect.y - 20, self.maxhealth, 5])
    def update_animation(self):
        self.animate()

    def launch_projectile(self, dir):
        self.all_projectiles.add(self.attack1(self, dir))
        self.start_animation()


class Player2(pygame.sprite.Sprite):
    def __init__(self, classe, game):
        super().__init__()
        self.health = 100
        self.maxhealth = 100
        self.all_projectiles = pygame.sprite.Group()
        self.attack = 50
        self.velocity = 5

        self.isJump = False
        self.jumpEnd = time.time()

        self.game = game
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

    def damage(self, amount):
        self.health -= amount