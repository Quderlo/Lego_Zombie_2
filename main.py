import sys
import pygame
from game_background import Background, get_font, menu_BG
from player import screen, player, player2
from constants import width, height, bg_size_x, bg_size_y
from button import Button
from enemy.enemy import zombie
from math import sqrt
from collision import col
from pygame import mixer

stop = True

pygame.init()
pygame.display.set_caption("POVT.EXE")
in_game_Background = Background


def play_solo():
    # Background music
    """pygame.display.set_caption("Play")
    mixer.music.load('assets/sounds/ambient/dungeon002.ogg')
    mixer.music.set_volume(0.2)
    mixer.music.play(-1)"""
    main_menu_music.stop()

    while True:
        for i in range(int(height / bg_size_y) + 1):
            for j in range(int(width / bg_size_x) + 1):
                screen.blit(in_game_Background[i][j].get_texture(),
                            (in_game_Background[i][j].get_rect().x, in_game_Background[i][j].get_rect().y))

        for i in zombie:
            i.render_zombie()
            if not i.attack_player(player.rect):
                i.move(player.rect.x, player.rect.y, col(i, zombie + [Background[5][5]]))

        player.movement(col(player, zombie + [Background[5][5]]))
        player.render_player()

        pygame.time.delay(15)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def dist(pos):
    zombie_to_player1_dist = int(sqrt((pos.rect.x - player.rect.x) ** 2 + (pos.rect.y - player.rect.y) ** 2))
    zombie_to_player2_dist = int(sqrt((pos.rect.x - player2.rect.x) ** 2 + (pos.rect.y - player2.rect.y) ** 2))
    return zombie_to_player1_dist > zombie_to_player2_dist


def play_duo():
    while True:
        for i in range(int(height / bg_size_y) + 1):
            for j in range(int(width / bg_size_x) + 1):
                screen.blit(in_game_Background[i][j].get_texture(),
                            (in_game_Background[i][j].get_rect().x, in_game_Background[i][j].get_rect().y))

        for i in zombie:
            i.render_zombie()

            if (not i.attack_player(player.rect)) and (not i.attack_player(player2.rect)):
                if dist(i):
                    i.move(player2.rect.x, player2.rect.y, col(i, zombie + [Background[5][5]]))
                else:
                    i.move(player.rect.x, player.rect.y, col(i, zombie + [Background[5][5]]))

        player.render_player()
        player2.render_player()

        player.movement(col(player, [player, player2] + zombie + [Background[5][5]]))
        player2.movement(col(player2, [player, player2] + zombie + [Background[5][5]]))

        pygame.time.delay(15)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


button_click = pygame.mixer.Sound("assets/sounds/main_menu/button_click.mp3")
button_click.set_volume(0.3)

button_hover = pygame.mixer.Sound("assets/sounds/main_menu/button_hover.mp3")
button_hover.set_volume(0.2)

main_menu_music = pygame.mixer.Sound("assets/sounds/main_menu/main_menu_music.mp3")
main_menu_music.set_volume(0.08)

button_hover_state_solo = False
button_hover_state_duo = False
button_hover_state_exit = False


def main_menu():
    main_menu_music.play()
    global button_hover_state_solo, button_hover_state_duo, button_hover_state_exit
    while True:
        screen.blit(menu_BG, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()
        current_hover_play_solo = 354 <= pygame.mouse.get_pos()[0] <= 500 + 284 / 2 and 339 <= pygame.mouse.get_pos()[
            1] <= 418
        current_hover_play_duo = 354 <= pygame.mouse.get_pos()[0] <= 500 + 284 / 2 and 462 <= pygame.mouse.get_pos()[
            1] <= 539
        current_hover_play_exit = 354 <= pygame.mouse.get_pos()[0] <= 500 + 284 / 2 and 582 <= pygame.mouse.get_pos()[
            1] <= 659

        # Hover sound for play_solo
        if current_hover_play_solo and not button_hover_state_solo:
            button_hover.play(0)
            button_hover_state_solo = True
        elif not current_hover_play_solo and button_hover_state_solo:
            button_hover_state_solo = False
        # Hover sound for play_duo
        if current_hover_play_duo and not button_hover_state_duo:
            button_hover.play(0)
            button_hover_state_duo = True
        elif not current_hover_play_duo and button_hover_state_duo:
            button_hover_state_duo = False
        # Hover sound for exit
        if current_hover_play_exit and not button_hover_state_exit:
            button_hover.play(0)
            button_hover_state_exit = True
        elif not current_hover_play_exit and button_hover_state_exit:
            button_hover_state_exit = False

        # print(menu_mouse_pos)

        play_button = Button(image=pygame.image.load("assets/images/main_menu/button.png"), pos=(500, 380),
                             text_input="Play solo", font=get_font(32), base_color="White", hovering_color="#43f1f8")
        duo_button = Button(image=pygame.image.load("assets/images/main_menu/button.png"), pos=(500, 500),
                            text_input="Play duo", font=get_font(32), base_color="White", hovering_color="#43f1f8")
        exit_button = Button(image=pygame.image.load("assets/images/main_menu/button.png"), pos=(500, 620),
                             text_input="Exit", font=get_font(32), base_color="White", hovering_color="#43f1f8")

        for button in [play_button, duo_button, exit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                    button_click.play()
                    play_solo()
                if duo_button.checkForInput(menu_mouse_pos):
                    button_click.play()
                    play_duo()
                if exit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
