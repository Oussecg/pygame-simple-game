import pygame

from player import Player
from rocket import Rocket
from time import time

class Game:
    def __init__(self):
        self.default_add_increment = 4000
        self.add_increment = self.default_add_increment
        self.max_speed = 2000
        self.count = 0
        self.start_time = time()
        self.elapsed_time = 0
        self.font = pygame.font.SysFont('comicsans', 30)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Dodge")
        self.background = pygame.image.load("assets/images/bg.jpeg").convert()
        self.background = pygame.transform.scale(self.background, self.screen.get_size())
        self.player = Player()
        self.rocket = Rocket()
        self.text = self.font.render(f'Time: {self.elapsed_time}s', True, (255, 255, 255))
        self.live_text = self.font.render(f"Lives: {self.player.lives}", True, "white")
        self.fps = 60
        self.rockets = pygame.sprite.Group()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        self.elapsed_time = round(time() - self.start_time) * 1000
        if self.add_increment > self.max_speed:
            self.add_increment = self.default_add_increment
            self.add_increment -= self.elapsed_time // 100
        self.count = self.elapsed_time // self.add_increment
        self.text = self.font.render(f'Time: {self.elapsed_time // 1000}s', True, (255, 255, 255))
        self.live_text = self.font.render(f"Lives: {self.player.lives}", True, "red")

        for rocket in self.rockets:
            rocket.update()
            if rocket.rect.bottom >= pygame.display.get_surface().get_height():
                self.rockets.remove(rocket)
                self.count -= 1
            elif rocket.rect.colliderect(self.player.rect):
                self.player.lives -= 1
                self.rockets.remove(rocket)
                self.count -= 1

        for z in range(self.count - len(self.rockets)):
            self.rockets.add(Rocket())

        self.player.check_live()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.player.move_left()
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.move_right()

    def render(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.player.img, self.player.rect)
        self.screen.blit(self.text, (10, 10))
        self.screen.blit(self.live_text, (pygame.display.get_surface().get_width() - (self.live_text.get_width() + 10), 10))
        self.rockets.draw(self.screen)
        self.clock.tick(self.fps)



