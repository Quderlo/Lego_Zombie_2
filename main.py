import sys

import pygame
from game_background import Background, get_font
from player import Player, Player2, screen
from constants import width, height, player_size
from button import Button


pygame.init()
pygame.display.set_caption("Menu")

player1_x = width / 2 - player_size
player1_y = height / 2 - player_size

in_game_Background = Background  # TODO: Убрать все загрузки картинок в отдельный файл
menu_BG = pygame.image.load('images/main_menu.jpg').convert() # Это в game_bg.py
player1_texture = pygame.image.load('images/player1.jpg').convert() # Что что а свой цвет игрок наверное знать должен
player2_texture = pygame.image.load('images/player2.jpg').convert()

player = Player(player1_texture, player1_x, player1_y)
player2 = Player2(player2_texture, player1_x, player1_y)


def play_solo():
    pygame.display.set_caption("Play")

    while True:
        for i in range(6):
            for j in range(8):
                screen.blit(in_game_Background[i][j].coord[2],
                            (in_game_Background[i][j].coord[0], in_game_Background[i][j].coord[1]))

        player.movement()

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def play_duo():
    while True:
        for i in range(6):
            for j in range(8):
                screen.blit(in_game_Background[i][j].coord[2],
                            (in_game_Background[i][j].coord[0], in_game_Background[i][j].coord[1]))

        player.movement()
        player2.movement()

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def main_menu():
    while True:
        screen.blit(menu_BG, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()

        play_button = Button(image=pygame.image.load("images/button.png"), pos=(150, 100),
                             text_input="Play solo", font=get_font(32), base_color="#77DDE7", hovering_color="White")
        duo_button = Button(image=pygame.image.load("images/button.png"), pos=(150, 200),
                            text_input="Play duo", font=get_font(32), base_color="#77DDE7", hovering_color="White")
        exit_button = Button(image=pygame.image.load("images/button.png"), pos=(150, 300),
                             text_input="Exit", font=get_font(32), base_color="#77DDE7", hovering_color="White")

        for button in [play_button, duo_button, exit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                    play_solo()
                if duo_button.checkForInput(menu_mouse_pos):
                    play_duo()
                if exit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
