import pygame
from spriteSheet import SpriteSheet
from time import time

class Explosion(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/spritsheet.png")
        self.spriteSheet = SpriteSheet(self.image)
        self.listImage = []
        self.start_animation_time = time()
        self.animation_time = 50
        self.frame = 0

        for x in range(12):
            self.listImage.append(self.spriteSheet.get_image(x, 128, 128, 1, "black"))

        self.image = self.listImage[0]
        self.rect = self.image.get_rect(topleft=(0, 0))

    def animate(self):
        if round((time() - self.start_animation_time) * 1000) >= self.animation_time:
            self.start_animation_time = time()
            self.frame += 1
            if self.frame >= 11:
                return True
            else:
                self.image = self.listImage[self.frame]
                return False