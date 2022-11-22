import pygame
from players import Player1, Player2


class Game:
    def __init__(self):
        self.player1 = Player1("guerrier")
        self.player2 = Player2("guerrier")
        self.pressed = {}