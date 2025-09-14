import pygame
from time import time

class Rockets:
    max_max_speed = 15
    max_rocket_speed = 9
    min_rocket_speed = 3
    start_time = time()
    is_max_speed = False
    
    def __init__(self):
        self.current_time = Rockets.start_time
        self.origin_img = pygame.image.load('assets/images/meteor.png').convert_alpha()
        self.origin_img = pygame.transform.scale(self.origin_img, (20, 20))

    def add_speed(self):
        complete = False
        max_speed = self.max_rocket_speed
        min_speed = self.min_rocket_speed
        self.elapsed_time = time() - self.start_time
        add_speed = self.elapsed_time / 1000
        if self.max_max_speed >= max_speed + add_speed:
            if time() - self.current_time >= 5:
                self.current_time = time()
                max_speed += add_speed
                min_speed += add_speed
        else:
            max_speed = self.max_max_speed
            if time() - self.current_time >= 5 and complete == False:
                self.current_time = time()
                if min_speed + add_speed <= max_speed:
                    min_speed += add_speed
                else:
                    min_speed = self.max_max_speed
                    complete = True
        Rockets.max_rocket_speed = max_speed
        Rockets.min_rocket_speed = min_speed
        return max_speed, min_speed
