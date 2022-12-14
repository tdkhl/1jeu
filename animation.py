import pygame
import math
class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}/{sprite_name}.png')

        self.current_image = 1
        self.images = animations.get(sprite_name)
        self.animation = False

    def start_animation(self):
        self.animation = True
    def animate(self, loop = False):
        if(self.animation):

            self.current_image += 0.08

            if self.current_image >= len(self.images):
                self.current_image = 0
                if loop is False:
                    self.animation = False

            self.image = self.images[math.floor(self.current_image)]



 # fonction pour charger les images
def load_animation_images(sprite_name):
        images = []
        path = f'assets/{sprite_name}/{sprite_name}'

        for num in range(1,7):
            image_path = path + str(num) + '.png'

            images.append(pygame.image.load(image_path))

        return images

    # dictionnaire qui contient les images chargées


animations = {
            'warrior' : load_animation_images('warrior')
    }

