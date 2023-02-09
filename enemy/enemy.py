import pygame
pygame.init()

img = pygame.image.load("images/enemy.png")

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


zombie = Enemy(100, 100)
zombie_group = pygame.sprite.Group()