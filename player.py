import pygame
from time import time

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.max_lives = 10
        self.lives = self.max_lives
        self.original_img = pygame.image.load('assets/images/sprite.png').convert_alpha()
        self.original_img = pygame.transform.scale(self.original_img, (50, 50))
        self.img = self.original_img
        self.positionX = pygame.display.get_surface().get_width() // 2
        self.positionY = pygame.display.get_surface().get_height() - 1
        self.rect = self.img.get_rect(midbottom=(self.positionX, self.positionY))
        self.velocity = [5, 0]
        self.angle = 0
        self.rotation_Speed = 5
        self.time = time()

    def move_left(self):
        if 0 < self.rect.left + self.velocity[0]:
            self.rect.x -= self.velocity[0]
            self.angle += self.rotation_Speed
            self.img = pygame.transform.rotate(self.original_img, self.angle)
            self.rect = self.img.get_rect(center=self.rect.center)

    def move_right(self):
        if self.rect.right - self.velocity[0] < pygame.display.get_surface().get_width():
            self.rect.x += self.velocity[0]
            self.angle -= self.rotation_Speed
            self.img = pygame.transform.rotate(self.original_img, self.angle)
            self.rect = self.img.get_rect(center=self.rect.center)

    def animation_damage(self):
        if round(time() - self.time) * 1000 >= 400:
            self.time = time()
            if self.img.get_alpha() == 255:
                self.img.set_alpha(128)
            else:
                self.img.set_alpha(255)
