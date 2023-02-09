import pygame
from constants import bg_size_x, bg_size_y, height, width
from player import screen

pygame.init()

Background = []
menu_BG = pygame.image.load('images/main_menu.jpg').convert() # Это в game_bg.py


class Bg(object):  # Описание заднего фона
    def __init__(self, x, y):
        self.texture = pygame.image.load('images/wall.jpg').convert()
        self.texture = pygame.transform.scale(self.texture, (bg_size_x, bg_size_y))
        self.rect = self.texture.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pass_on = True

    def get_rect(self):
        return self.rect

    def get_texture(self):
        return self.texture

    def hui(self):  # TODO: Переименовать
        return self.pass_on


class Fence(object):
    def __init__(self, x, y):
        self.texture = pygame.image.load('images/fence.jpg').convert()  # TODO: Сделать картинку забора
        self.texture = pygame.transform.scale(self.texture, (bg_size_x, bg_size_y))
        self.rect = self.texture.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pass_on = False

    def get_rect(self):
        return self.rect

    def get_texture(self):
        return self.texture

    def hui(self):  # TODO: Переименовать
        return self.pass_on


for i in range(int(height / bg_size_x)):  # Заполнение карты (создание двойного массива с блоками)
    Background.append([])
    for j in range(int(width / bg_size_y)):
        if ((j == 0) or (j == int(height / bg_size_y) - 1)) and \
                (i != int(width / bg_size_x) / 2) and (i != int(width / bg_size_x) / 2 - 1):
            Background[i].append(Fence(i * bg_size_x, j * bg_size_y))
        else:
            Background[i].append(Bg(i * bg_size_x, j * bg_size_y))


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)
