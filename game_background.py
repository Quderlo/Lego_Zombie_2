import pygame
from constants import bg_size_x, bg_size_y
from player import screen

pygame.init()


class Bg(object):  # Описание заднего фона
    def __init__(self, x, y, texture):
        self.coord = [x, y, texture]


Background = []
img = pygame.image.load('images/wall.jpg').convert()

for i in range(6):  # Заполнение карты (создание двойного массива с блоками)
    Background.append([])
    for j in range(8):
        Background[i].append(Bg(j * bg_size_y, i * bg_size_x, img))


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)