import pygame

from player import Player
from rocket import Rocket
from explosion import Explosion
from time import time

class Game:
    def __init__(self):
        self.game_started = False
        self.game_finished = False
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
        self.explosion = Explosion()
        self.text = self.font.render(f'Time: {self.elapsed_time}s', True, (255, 255, 255))
        self.live_text = self.font.render(f"Lives: {self.player.lives}", True, "white")
        self.fps = 60
        self.rockets = pygame.sprite.Group()
        self.start_button = pygame.image.load("assets/images/start.png").convert()
        self.start_button = pygame.transform.scale(self.start_button, (200, 100))
        self.start_button_x = (pygame.display.get_surface().get_width() - self.start_button.get_width()) // 2
        self.start_button_y = (pygame.display.get_surface().get_height() - self.start_button.get_height()) // 2
        self.start_button_rect = self.start_button.get_rect(topleft=(self.start_button_x, self.start_button_y))
        self.game_over_image = pygame.image.load("assets/images/glitch-game-background.jpg")
        self.game_over_image = pygame.transform.scale(self.game_over_image, (800, 600))
        self.game_over_image_x = (pygame.display.get_surface().get_width() - self.game_over_image.get_width()) // 2
        self.game_over_image_y = (pygame.display.get_surface().get_height() - self.game_over_image.get_height()) // 2
        self.game_over_image_rect = self.game_over_image.get_rect(topleft=(self.game_over_image_x, self.game_over_image_y))
        self.explosions = pygame.sprite.Group()

    def check_events(self):
        if self.game_started:
            # this is the counter time
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
                    self.count -= 1
                    explosion = Explosion()
                    explosion.rect.x, explosion.rect.y = rocket.rect.x, rocket.rect.bottom - explosion.rect.height
                    self.rockets.remove(rocket)
                    self.explosions.add(explosion)
                elif rocket.rect.colliderect(self.player.rect):
                    self.player.lives -= 1
                    self.rockets.remove(rocket)
                    self.count -= 1

            for _ in range(self.count - len(self.rockets)):
                self.rockets.add(Rocket())

            for explosion in self.explosions:
                if explosion.animate():
                    self.explosions.remove(explosion)

            self.check_live()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_q]:
                self.player.move_left()
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.player.move_right()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button_rect.collidepoint(event.pos):
                    self.game_started = True

    def render(self):
        if self.game_started and not self.game_finished:
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.player.img, self.player.rect)
            self.screen.blit(self.text, (10, 10))
            self.screen.blit(self.live_text, (pygame.display.get_surface().get_width() - (self.live_text.get_width() + 10), 10))
            self.rockets.draw(self.screen)
            self.explosions.draw(self.screen)
            self.clock.tick(self.fps)
        elif not self.game_started and not self.game_finished:
            self.screen.blit(self.start_button, self.start_button_rect)
        elif self.game_finished:
            self.screen.blit(self.game_over_image, self.game_over_image_rect)

    def check_live(self):
        if self.player.lives <= 0:
            self.screen.fill("black")
            self.game_started = False
            self.game_finished = True


