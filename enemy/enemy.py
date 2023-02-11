from constants import collision_tolerance
import pygame
from player import screen
import random


pygame.init()

img = pygame.image.load("images/enemy.png")


class Enemy(object):
    def __init__(self, x, y):
        self.img = pygame.transform.scale(img, (60, 60))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y

    def render_zombie(self):
        screen.blit(self.img, self.rect)

    def move(self, kek_x, kek_y):
        if (kek_x > self.rect.x):
            self.rect.x += 1
        if (kek_y > self.rect.y):
            self.rect.y += 1
        if (kek_x < self.rect.x):
            self.rect.x -= 1
        if (kek_y < self.rect.y):
            self.rect.y -= 1

    def attack_player(self, player_rect):  # TODO: Добавить анимации для зомби
        if pygame.Rect.colliderect(player_rect, self.rect):
            if abs(player_rect.top - self.rect.bottom) < collision_tolerance:
                #player_lose_hp(На сколько уменьшится хп) TODO: Добавить потерю здоровья игрока
                # анимация атаки зомби сверху вниз
                return True
            elif abs(player_rect.bottom - self.rect.top) < collision_tolerance:
                # анимация атаки зомби снизу вверх
                return True
            elif abs(player_rect.left - self.rect.right) < collision_tolerance:
                # анимация атаки зомби справа налево
                return True
            elif abs(player_rect.right - self.rect.left) < collision_tolerance:
                # анимация атаки зомби слево направо
                return True
            else:
                # анимация атаки зомби слево направо
                return True
        else:
            return False


zombie = []
for i in range(2):
    z = Enemy(random.randint(0, 500), random.randint(0, 500))
    zombie.append(z)


