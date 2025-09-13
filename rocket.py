import pygame
from rockets import Rockets
from random import randint

class Rocket(pygame.sprite.Sprite, Rockets):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        Rockets.__init__(self)
        self.image = self.origin_img
        self.positionX = randint(0, pygame.display.get_surface().get_width() - self.image.get_width())
        self.positionY = -self.origin_img.get_height()
        self.rect = self.image.get_rect(topleft=(self.positionX, self.positionY))
        self.max_speed, self.min_speed = self.add_speed()
        self.y_speed = randint(round(self.min_speed), round(self.max_speed))
        self.velocity = [0, self.y_speed]
        self.on_move = True

    def move(self):
        if self.on_move:
            self.rect.y += self.velocity[1]

    def update(self):
        self.move()

