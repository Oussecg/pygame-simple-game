import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_img = pygame.image.load('assets/images/sprite.png').convert_alpha()
        self.original_img = pygame.transform.scale(self.original_img, (50, 50))
        self.img = self.original_img
        self.positionX = pygame.display.get_surface().get_width() // 2
        self.positionY = pygame.display.get_surface().get_height() - 1
        self.rect = self.img.get_rect(midbottom=(self.positionX, self.positionY))
        self.velocity = [0, 0]
        self.angle = 0
        self.rotation_Speed = 0
        self.on_move = False

    def move(self):
        if self.on_move:
            self.rect.x += self.velocity[0]
            self.angle += self.rotation_Speed

            self.img = pygame.transform.rotate(self.img, self.angle)

    def update(self):
        self.move()
        self.img = pygame.transform.rotate(self.original_img, self.angle)
        self.rect = self.img.get_rect(center=self.rect.center)