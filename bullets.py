import pygame
from constants import bullet_speed
from screen import screen


class Bullet(object):
    def __init__(self, player):
        self.image = pygame.image.load('assets/images/other_img/bullet.jpg').convert()
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.centerx
        self.rect.y = player.rect.centery
        self.speed = bullet_speed
        self.vel = (player.side[0] * self.speed, player.side[1] * self.speed)  # Направление полёта снаряда * на скорость

    def render(self):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]


