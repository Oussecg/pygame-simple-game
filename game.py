import pygame
from player import Player

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Dodge")
        self.background = pygame.image.load("assets/images/bg.jpeg").convert()
        self.background = pygame.transform.scale(self.background, self.screen.get_size())
        self.player = Player()

    def render(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.player.img, self.player.rect)
        pygame.display.flip()
        self.clock.tick(60)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.velocity[0] = -5
                    self.player.rotation_Speed = 10
                    self.player.on_move = True
                elif event.key == pygame.K_RIGHT:
                    self.player.velocity[0] = 5
                    self.player.rotation_Speed = -10
                    self.player.on_move = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.player.velocity[0] = 0
                    self.player.rotation_Speed = 0
                    self.player.on_move = False
