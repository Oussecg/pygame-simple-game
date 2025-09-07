import pygame
from game import Game

pygame.init()
pygame.font.init()
game = Game()


print(game.start_button_rect.x)
print(game.start_button_rect.y)

while True:
    game.check_events()
    game.render()
    pygame.display.flip()
