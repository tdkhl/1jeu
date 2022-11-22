import pygame

# Classe Projectile Guerrier

class ProjectileWarrior(pygame.sprite.Sprite):
    def __init__(self, player, dir):
        super().__init__()
        self.velocity = 2
        self.image = pygame.image.load('assets/warrior/arrow.png')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 50
        self.origin_image = self.image
        self.angle = 0
        self.player = player
        self.dir = dir


        if dir == "gauche":
            self.image = pygame.transform.rotate(self.image, 180)

    def rotate(self):
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.ange, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)
    def move(self):
        if self.dir == "gauche":
            self.rect.x -= self.velocity
        else:
            self.rect.x += self.velocity
        if self.rect.x > 1280 or self.rect.x < 0:
            self.remove()