import sys
import pygame
from game_background import Background, get_font, menu_BG
from player import screen, player, player2
from constants import width, height, bg_size_x, bg_size_y
from button import Button
from enemy.enemy import zombie
from math import sqrt
from collision import col

stop = True

pygame.init()
pygame.display.set_caption("Menu")
in_game_Background = Background


def play_solo():
    pygame.display.set_caption("Play")

    while True:
        for i in range(int(height / bg_size_y)):
            for j in range(int(width / bg_size_x)):
                screen.blit(in_game_Background[i][j].get_texture(),
                            (in_game_Background[i][j].get_rect().x, in_game_Background[i][j].get_rect().y))

        for i in zombie:
            i.render_zombie()
            if not i.attack_player(player.rect):
                i.move(player.rect.x, player.rect.y, col(i, zombie))

        player.movement()
        player.render_player()

        pygame.time.delay(15)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def dist(pos):
    zombie_to_player1_dist = int(sqrt((pos.rect.x - player.rect.x) ** 2 + (pos.rect.y - player.rect.y)**2))
    zombie_to_player2_dist = int(sqrt((pos.rect.x - player2.rect.x) ** 2 + (pos.rect.y - player2.rect.y)**2))
    return zombie_to_player1_dist > zombie_to_player2_dist


def play_duo():
    while True:
        for i in range(int(height / bg_size_y)):
            for j in range(int(width / bg_size_x)):
                screen.blit(in_game_Background[i][j].get_texture(),
                            (in_game_Background[i][j].get_rect().x, in_game_Background[i][j].get_rect().y))

        for i in zombie:
            i.render_zombie()

            if (not i.attack_player(player.rect)) and (not i.attack_player(player2.rect)):
                if dist(i):
                    i.move(player2.rect.x, player2.rect.y, col(i, zombie))
                else:
                    i.move(player.rect.x, player.rect.y, col(i, zombie))

        player.render_player()
        player2.render_player()
        player.movement()
        player2.movement()

        pygame.time.delay(15)
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
