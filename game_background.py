import pygame
from constants import bg_size_x, bg_size_y, height, width
from screen import screen

Background = []
esc_menu = pygame.image.load("assets/images/main_menu/escape_menu.jpg")
menu_BG = pygame.image.load('assets/images/main_menu/menu_background.jpg').convert()


class Floor(object):  # Описание заднего фона
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


for i in range(int(height / bg_size_x) + 1):  # Заполнение карты (создание двойного массива с блоками)
    Background.append([])
    for j in range(int(width / bg_size_y) + 1):
            floor = Floor(i * bg_size_x, j * bg_size_y)
            Background[i].append(floor)

"""for i in range(4):  # Заполнение карты (создание двойного массива с блоками)
    for j in range(1):
        Background[i][j] = Fence(i * bg_size_x, j * bg_size_y)"""

for i in range(6, 10, 1):  # Заполнение карты (создание двойного массива с блоками)
    for j in range(1):
        Background[i][j] = Fence(i * bg_size_x, j * bg_size_y)
for i in range(0, 4, 1):  # Заполнение карты (создание двойного массива с блоками)
    for j in range(1):
        Background[i][j] = Fence(i * bg_size_x, j * bg_size_y)

for i in range(6, 10, 1):  # Заполнение карты (создание двойного массива с блоками)
        Background[i][9] = Fence(i * bg_size_x, 9 * bg_size_y)

for i in range(0, 4, 1):  # Заполнение карты (создание двойного массива с блоками)
        Background[i][9] = Fence(i * bg_size_x, 9 * bg_size_y)


Background[5][5] = Fence(5 * bg_size_x, 5 * bg_size_y)
bg_col = []

for i in range(int(height / bg_size_x) + 1):
    for j in range(int(width / bg_size_y) + 1):
        if not Background[i][j].pass_on:
            bg_col.append(Background[i][j])


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)