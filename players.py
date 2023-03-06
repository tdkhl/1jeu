import pygame
from projectiles import ProjectileWarrior, InvincibiliteWarrior, ProjectileAssassin
import time
import animation
import sys

class Player1(animation.AnimateSprite):
    def __init__(self, classe, game):
        self.attack1 = None
        if classe == "guerrier":
            super().__init__("warrior")

            self.attack1 = ProjectileWarrior
            self.attack3 = InvincibiliteWarrior

        self.health = 100
        self.maxhealth = 100
        self.all_projectiles = pygame.sprite.Group()
        self.attack = 10
        self.velocity = 2
        self.isJump = False
        self.jumpEnd = time.time()
        self.game = game
        self.rect = self.image.get_rect()
        self.rect.y = 400
        self.Alive = True


        self.attack1_cd = 1.5
        self.attack1_last_use = time.time() - 5
        self.attack3_cd = 20
        self.attack3_last_use = time.time() - 20
        self.InvincibiliteWarrior = False

    def move_right(self):
        if not self.Alive:
            return
        self.rect.x += self.velocity
        if self.isJump:
            self.start_animation_jump()
        else:
            self.start_animation_walk()


    def move_left(self):
        if not self.Alive:
            return
        self.rect.x -= self.velocity
        if self.isJump:

            self.start_animation_jump_gauche()
        else:
            self.start_animation_walk_gauche()


    def move_up(self):
        if not self.Alive:
            return
        self.isJump = True
        self.jumpEnd = time.time() + 1
        #self.start_animation_jump()

    def damage(self, amount):
        if not self.Alive:
            return
        if self.health <= 0:
            self.start_animation_death()
            self.Alive = False
        if (self.InvincibiliteWarrior):
            if (self.InvincibiliteWarriorTime < time.time()):
                self.InvincibiliteWarrior = False
        else:
            self.health -= amount

    def update_health_bar(self, surface):
        if not self.Alive:
            return
        if (self.InvincibiliteWarrior):
            pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 20, self.rect.y - 20, self.maxhealth, 5])
            pygame.draw.rect(surface, (255, 215, 0), [self.rect.x + 20, self.rect.y - 20, self.health, 5])
        else:
            pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 20, self.rect.y - 20, self.maxhealth, 5])
            pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 20, self.rect.y - 20, self.health, 5])

    def update_animation(self):
        self.animate()

    def launch_projectile(self, dir):
        if not self.Alive:
            return
        self.all_projectiles.add(self.attack1(self, dir))
        self.start_animation()

    def launch_attack3(self):
        if not self.Alive:
            return
        self.attack3(self)


class Player2(animation.AnimateSprite):
    def __init__(self, classe, game):
        self.attack1 = None
        if classe == "assassin":
            super().__init__("assassin")

            self.attack1 = ProjectileAssassin
            self.attack3 = InvincibiliteWarrior

        self.health = 100
        self.maxhealth = 100
        self.all_projectiles = pygame.sprite.Group()
        self.attack = 10
        self.velocity = 2
        self.isJump = False
        self.jumpEnd = time.time()
        self.game = game
        self.rect = self.image.get_rect()
        self.rect.y = 400
        self.rect.x = 1100

        self.Alive = True



        self.attack1_cd = 1.5
        self.attack1_last_use = time.time() - 5
        self.attack3_cd = 20
        self.attack3_last_use = time.time() - 20
        self.InvincibiliteWarrior = False


    def move_right(self):
        if not self.Alive:
            return
        self.rect.x += self.velocity
        if self.isJump:
            self.start_animation_jump()
        else:
            self.start_animation_walk()


    def move_left(self):
        if not self.Alive:
            return
        self.rect.x -= self.velocity
        if self.isJump:

            self.start_animation_jump_gauche()
        else:
            self.start_animation_walk_gauche()


    def move_up(self):
        if not self.Alive:
            return
        self.isJump = True
        self.jumpEnd = time.time() + 1
        #self.start_animation_jump()

    def damage(self, amount):
        if (self.InvincibiliteWarrior):
            if (self.InvincibiliteWarriorTime < time.time()):
                self.InvincibiliteWarrior = False

        if (self.health - amount) <= 0:
            self.start_animation_death()
            self.Alive = False

        else:
            self.health -= amount

    def update_health_bar(self, surface):
        if not self.Alive:
            return
        if (self.InvincibiliteWarrior):
            pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 20, self.rect.y - 20, self.maxhealth, 5])
            pygame.draw.rect(surface, (255, 215, 0), [self.rect.x + 20, self.rect.y - 20, self.health, 5])
        else:
            pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 20, self.rect.y - 20, self.maxhealth, 5])
            pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 20, self.rect.y - 20, self.health, 5])

    def update_animation(self):
        self.animate()

    def launch_projectile(self, dir):
        if not self.Alive:
            return
        self.all_projectiles.add(self.attack1(self, dir))
        self.start_animation()

    def launch_attack3(self):
        if not self.Alive:
            return
        self.attack3(self)

