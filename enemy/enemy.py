from constants import collision_tolerance
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

    def render_zombie(self):
        screen.blit(self.img, self.rect)

    def move(self, kek_x, kek_y):
        if kek_x > self.rect.x:
            self.rect.x += 1
        if kek_y > self.rect.y:
            self.rect.y += 1
        if kek_x < self.rect.x:
            self.rect.x -= 1
        if kek_y < self.rect.y:
            self.rect.y -= 1

    def attack_player(self, player_rect):  # TODO: Добавить анимации для зомби
        if pygame.Rect.colliderect(player_rect, self.rect):
            if abs(player.rect.top - zombie.rect.bottom) < collision_tolerance:
                #player_lose_hp(На сколько уменьшится хп) TODO: Добавить потерю здоровья игрока
                print('you_lose') # Игрок теряет хп
                # анимация атаки зомби сверху вниз
                return [True, "top"]
            elif abs(player.rect.bottom - zombie.rect.top) < collision_tolerance:
                print('you_lose')  # Игрок теряет хп
                # анимация атаки зомби снизу вверх
                return [True, "bottom"]
            elif abs(player.rect.left - zombie.rect.right) < collision_tolerance:
                print('you_lose')  # Игрок теряет хп
                # анимация атаки зомби справа налево
                return [True, "right"]
            elif abs(player.rect.right - zombie.rect.left) < collision_tolerance:
                print('you_lose')  # Игрок теряет хп
                # анимация атаки зомби слево направо
                return [True, "left"]
            else:
                return [True, "inside"]
        else:
            return [False, "none"]


zombie = Enemy(50, 50)
