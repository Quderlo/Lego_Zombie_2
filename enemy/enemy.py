import pygame
from player import player

pygame.init()

img = pygame.image.load("images/enemy.png")




class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_coord(self):
        coord_x = self.rect.x
        coord_y = self.rect.y

        return [coord_x, coord_y]

    def move(self, kek_x, kek_y):
        if kek_x > self.rect.x:
            self.rect.x += 1
        if kek_y > self.rect.y:
            self.rect.y += 1
        if kek_x < self.rect.x:
            self.rect.x -= 1
        if kek_y < self.rect.y:
            self.rect.y -= 1


zombie = Enemy(50, 50)
zombie_group = pygame.sprite.Group()
