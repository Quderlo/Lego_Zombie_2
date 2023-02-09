import sys

import pygame
from game_background import Background, get_font, menu_BG
from player import screen, player, player2
from constants import width, height, bg_size_x, bg_size_y
from button import Button
from enemy.enemy import zombie, zombie_group


pygame.init()
pygame.display.set_caption("Menu")
in_game_Background = Background  # TODO: Убрать все загрузки картинок в отдельный файл


def play_solo():
    pygame.display.set_caption("Play")

    while True:
        for i in range(int(height / bg_size_y)):
            for j in range(int(width / bg_size_x)):
                screen.blit(in_game_Background[i][j].get_texture(),
                            (in_game_Background[i][j].get_rect().x, in_game_Background[i][j].get_rect().y))

        player.movement()

        zombie
        zombie_group.add(zombie)
        zombie_group.draw(screen)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def play_duo():
    while True:
        for i in range(int(height / bg_size_y)):
            for j in range(int(width / bg_size_x)):
                screen.blit(in_game_Background[i][j].get_texture(),
                            (in_game_Background[i][j].get_rect().x, in_game_Background[i][j].get_rect().y))

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
