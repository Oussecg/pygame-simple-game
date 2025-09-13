import pygame
from random import randint
from time import time

class Rocket(pygame.sprite.Sprite):
    def __init__(self, elapsed_time = ""):
        super().__init__()
        self.elapsed_time = elapsed_time
        self.current_time = self.elapsed_time
        self.max_speed = 9
        self.min_speed = 3
        self.origin_img = pygame.image.load('assets/images/meteor.png').convert_alpha()
        self.origin_img = pygame.transform.scale(self.origin_img, (20, 20))
        self.image = self.origin_img
        self.positionX = randint(0, pygame.display.get_surface().get_width() - self.image.get_width())
        self.positionY = -self.origin_img.get_height()
        self.rect = self.image.get_rect(topleft=(self.positionX, self.positionY))
        self.add_speed()
        self.y_speed = randint(round(self.min_speed), round(self.max_speed))
        self.velocity = [0, self.y_speed]
        self.on_move = True

    def move(self):
        if self.on_move:
            self.rect.y += self.velocity[1]

    def update(self):
        self.move()
        #print(self.max_speed, self.min_speed, self.y_speed)

    def add_speed(self):
        add_speed = self.elapsed_time / 10000
        if 20 >= self.max_speed + add_speed:
            if time() - self.current_time >= 5:
                self.current_time = time()
                self.max_speed += add_speed
                self.min_speed += add_speed
        else:
            self.max_speed = 20
            if self.min_speed + add_speed <= self.max_speed:
                self.min_speed += add_speed
            else:
                self.min_speed = 20
        print(add_speed, self.max_speed, self.min_speed)

