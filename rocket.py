import pygame
from random import randint

class Rocket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.origin_img = pygame.image.load('assets/images/meteor.png').convert_alpha()
        self.origin_img = pygame.transform.scale(self.origin_img, (20, 20))
        self.image = self.origin_img
        self.positionX = randint(0, pygame.display.get_surface().get_width() - self.image.get_width())
        self.positionY = -self.origin_img.get_height()
        self.rect = self.image.get_rect(topleft=(self.positionX, self.positionY))
        self.velocity = [0, 9]
        self.on_move = True

    def move(self):
        if self.on_move:
            self.rect.y += randint(3, self.velocity[1])

    def update(self):
        self.move()
