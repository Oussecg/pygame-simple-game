import pygame
from game import Game

pygame.init()
game = Game()


while True:
    game.render()
    game.check_events()
    game.player.update()