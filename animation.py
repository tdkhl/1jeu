import pygame
import math
class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}/attaque/{sprite_name}.png')
        self.image_walk = pygame.image.load(f'assets/{sprite_name}/marcher/{sprite_name}.png')
        self.image_jump = pygame.image.load(f'assets/{sprite_name}/jump/{sprite_name}.png')
        self.image_death = pygame.image.load(f'assets/{sprite_name}/death/{sprite_name}.png')
        self.current_image = 1
        self.current_image_walk = 1
        self.current_image_jump = 1
        self.current_image_death = 1
        self.images = animations.get(sprite_name)
        self.images_walk = animations.get(f'{sprite_name}_walk')
        self.images_jump = animations.get(f'{sprite_name}_jump')
        self.images_death = animations.get(f'{sprite_name}_death')
        self.animation = False
        self.animation_walk = False
        self.animation_walk_gauche = False
        self.animation_jump = False
        self.animation_jump_gauche = False
        self.animation_death = False

    def start_animation(self):
        self.animation = True

    def start_animation_walk(self):
        self.animation_walk = True

    def start_animation_walk_gauche(self):
        self.animation_walk_gauche = True

    def start_animation_jump(self):
        self.animation_jump = True

    def start_animation_jump_gauche(self):
        self.animation_jump_gauche = True

    def start_animation_death(self):
        self.animation_death = True




    def animate(self, loop=False):
        if(self.animation):

            self.current_image += 0.15

            if self.current_image >= len(self.images):
                self.current_image = 0
                if loop is False:
                    self.animation = False

            self.image = self.images[math.floor(self.current_image)]

        if (self.animation_walk):

            self.current_image_walk += 0.1

            if self.current_image_walk >= len(self.images_walk):
                self.current_image_walk = 0
                if loop is False:
                    self.animation_walk = False

            self.image = self.images_walk[math.floor(self.current_image_walk)]

        if self.animation_walk_gauche:
            self.current_image_walk += 0.1

            if self.current_image_walk >= len(self.images_walk):
                self.current_image_walk = 0
                if loop is False:
                    self.animation_walk_gauche = False

            self.image = pygame.transform.flip(self.images_walk[math.floor(self.current_image_walk)],100, 0)

        if self.animation_jump_gauche:
            self.current_image_jump += 0.025

            if self.current_image_jump >= len(self.images_jump):
                self.current_image_jump = 0
                if loop is False:
                    self.animation_jump_gauche = False

            self.image = pygame.transform.flip(self.images_jump[math.floor(self.current_image_jump)], 100, 0)


        if (self.animation_jump):

            self.current_image_jump += 0.025

            if self.current_image_jump >= len(self.images_jump):
                self.current_image_jump = 0
                if loop is False:
                    self.animation_jump = False

            self.image = self.images_jump[math.floor(self.current_image_jump)]


        if (self.animation_death):

            self.current_image_death += 0.09

            if self.current_image_death >= len(self.images_death):
                self.current_image_death = 0
                if loop is False:
                    self.animation_death = False

            self.image = self.images_death[math.floor(self.current_image_death)]

 # fonction pour charger les images
def load_animation_images(sprite_name):
        images = []

        path = f'assets/{sprite_name}/attaque/{sprite_name}'
        for num in range(1,7):
            image_path = path + str(num) + '.png'

            images.append(pygame.image.load(image_path))

        return images


def load_animation_images_walk(sprite_name):
        images = []

        path = f'assets/{sprite_name}/marcher/{sprite_name}'

        for num in range(1, 9):
            image_path = path + str(num) + '.png'

            images.append(pygame.image.load(image_path))

        return images


def load_animation_images_jump(sprite_name):
        images = []

        path = f'assets/{sprite_name}/jump/{sprite_name}'

        for num in range(1, 9):
            image_path = path + str(num) + '.png'

            images.append(pygame.image.load(image_path))

        return images


def load_animation_images_death(sprite_name):
        images = []

        path = f'assets/{sprite_name}/death/{sprite_name}'

        for num in range(1, 9):
            image_path = path + str(num) + '.png'

            images.append(pygame.image.load(image_path))

        return images


    # dictionnaire qui contient les images chargées

animations = {
            'warrior': load_animation_images('warrior'),
            'warrior_walk': load_animation_images_walk('warrior'),
            'warrior_jump': load_animation_images_jump('warrior'),
            'warrior_death': load_animation_images_death('warrior'),
            'assassin': load_animation_images('assassin'),
            'assassin_walk': load_animation_images_walk('assassin'),
            'assassin_jump': load_animation_images_jump('assassin'),
            'assassin_death': load_animation_images_death('assassin')
    }



