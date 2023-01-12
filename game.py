import pygame
from players import Player1, Player2


class Game:
    def __init__(self):
        self.is_playing = False
        self.player1 = Player1("guerrier", self)
        self.player2 = Player2("guerrier", self)
        self.pressed = {}
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player1)
        self.all_players.add(self.player2)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def update(self, screen):
        # appliquer l'image de mon joueur
        screen.blit(self.player2.image, self.player2.rect)

        # actualiser l'animation du joueur
        self.player2.update_animation()