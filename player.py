import pygame
from constants import width, height, player_size

pygame.init()

screen = pygame.display.set_mode((width, height))


class Player(object):
    def __init__(self, texture, px, py):
        img = texture
        self.image = pygame.transform.scale(img, (player_size, player_size))
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py

    def move(self, diffx, diffy):
        self.rect.x += diffx
        self.rect.y += diffy

    def movement(self):
        screen.blit(self.image, self.rect)
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.move(-1, 0)
        if key[pygame.K_RIGHT]:
            self.move(1, 0)
        if key[pygame.K_UP]:
            self.move(0, -1)
        if key[pygame.K_DOWN]:
            self.move(0, 1)


class Player2(Player):
    def movement(self):
        screen.blit(self.image, self.rect)
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            self.move(-1, 0)
        if key[pygame.K_d]:
            self.move(1, 0)
        if key[pygame.K_w]:
            self.move(0, -1)
        if key[pygame.K_s]:
            self.move(0, 1)
