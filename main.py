import pygame
from game import Game

pygame.init()
pygame.font.init()
game = Game()


while True:
    game.check_events()
    game.render()
    pygame.display.flip()
