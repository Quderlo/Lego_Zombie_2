import time
import random
import pygame
from player import player
from player import screen

pygame.init()

img = pygame.image.load("images/enemy.png")


class Enemy(object):
    def __init__(self, x, y):
        self.img = pygame.transform.scale(img, (60, 60))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_coord(self):
        coord_x = self.rect.x
        coord_y = self.rect.y

        return [coord_x, coord_y]

    def move(self, kek_x, kek_y):
        screen.blit(self.img, self.rect)
        if kek_x > self.rect.x:
            self.rect.x += 1
        if kek_y > self.rect.y:
            self.rect.y += 1
        if kek_x < self.rect.x:
            self.rect.x -= 1
        if kek_y < self.rect.y:
            self.rect.y -= 1


zombie = Enemy(50, 50)

