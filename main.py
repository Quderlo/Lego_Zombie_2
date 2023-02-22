import sys
import threading
import time

import pygame

from game_background import Background, get_font, menu_BG, esc_menu
from main_menu_buttons import main_menu_music, button_click, main_menu_button, button_hover
from player import player, player2
from constants import width, height, bg_size_x, bg_size_y
from button import Button
from math import sqrt
from collision import col
from pygame import mixer
from enemy.zombie import zombie, matrix, num_of_enemies, t2
# from threading import Thread
from screen import screen
from pause import pause
from game_background import bg_col
from constants import player_size

pygame.init()
pygame.display.set_caption("POVT.EXE")
game_icon = programIcon = pygame.image.load('assets/images/game_icon.png')
pygame.display.set_icon(game_icon)
in_game_Background = Background
clock = pygame.time.Clock()

bool_of_move = True


def enemy_path_ai():
    while True:
        time.sleep(1)
        for i in range(10):
            # print(i)
            try:
                zombie[i].create_path(zombie[i].rect.x // 50, zombie[i].rect.y // 50, matrix, True, player.rect,
                                          col(zombie[i], zombie + [player] + bg_col))
            except:
                pass


def enemy_attack():
    global bool_of_move


    while True:
        time.sleep(2)
        jump_count = 10
        for i in range(len(zombie)):
            # zombie[i].self_distance(player)

            if zombie[i].self_distance(player) <= 100:
                near_zombie = zombie[i]
                bool_of_move = False

                if near_zombie.rect.y // player_size < player.rect.y // player_size:
                    for j in range(30):
                        player.move(0, 2, col(player, zombie + [player] + bg_col))
                        time.sleep(0.0025)

                elif near_zombie.rect.y // player_size > player.rect.y // player_size:
                    for j in range(30):
                        player.move(0, -2, col(player, zombie + [player] + bg_col))
                        time.sleep(0.0025)

                elif near_zombie.rect.x // player_size < player.rect.x // player_size:
                    for j in range(30):
                        player.move(2, 0, col(player, zombie + [player] + bg_col))
                        time.sleep(0.0025)

                elif near_zombie.rect.x // player_size > player.rect.x // player_size:
                    for j in range(30):
                        player.move(-2, 0, col(player, zombie + [player] + bg_col))
                        time.sleep(0.0025)

                player.helth -= 10  #TODO: enemy_damage
                time.sleep(0.5)

        bool_of_move = True


thr1 = threading.Thread(target=enemy_path_ai, daemon=True)
thr2 = threading.Thread(target=enemy_attack, daemon=True)


def play_solo():
    t2.start()
    thr1.start()
    thr2.start()
    # Background music
    start_round = pygame.mixer.Sound("assets/sounds/COD_start_round.mp3")
    start_round.set_volume(0.1)
    start_round.play()
    pygame.display.set_caption("Play")
    mixer.music.load('assets/sounds/ambient/ambience.mp3')
    mixer.music.set_volume(0.1)
    mixer.music.play(-1)
    main_menu_music.stop()
    bullets_list = []

    while True:
        get_fps = clock.get_fps()  # TODO: Поменяй       #TODO: это удалим потом
        pygame.display.set_caption("FPS: " + str(get_fps))
        id(matrix)
        matrix[10][10] = 0
        matrix[11][10] = 0
        matrix[11][11] = 0
        matrix[10][12] = 0

        esc_key = pygame.key.get_pressed()
        for i in range(int(height / bg_size_y)):
            for j in range(int(width / bg_size_x)):
                screen.blit(in_game_Background[i][j].get_texture(),
                            (in_game_Background[i][j].get_rect().x, in_game_Background[i][j].get_rect().y))

        player.movement(col(player, zombie + bg_col))
        player.render_player()

        # bullets_list = player.shoot(bullets_list, [zombie])
        # bullets_list, zombie = player.shoot(bullets_list, zombie)

        try:
            for i in range(num_of_enemies):
                zombie[i].update()
                zombie[i].movement(matrix, col(zombie[i], zombie + [player] + bg_col), bool_of_move)
        except:
            pass

        count_now = len(zombie)
        if count_now >= 10:
            for i in range(10, count_now):
                zombie[i].stupid_ai(player.rect, col(zombie[i], zombie + [player] + bg_col))
                pass

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if esc_key[pygame.K_ESCAPE]:
                start_round.stop()
                mixer.music.pause()
                pause()
            if event.type == pygame.USEREVENT:
                pass
        clock.tick(60)


def dist(pos):
    zombie_to_player1_dist = int(sqrt((pos.rect.x - player.rect.x) ** 2 + (pos.rect.y - player.rect.y) ** 2))
    zombie_to_player2_dist = int(sqrt((pos.rect.x - player2.rect.x) ** 2 + (pos.rect.y - player2.rect.y) ** 2))
    return zombie_to_player1_dist > zombie_to_player2_dist


def play_duo():
    # Background music
    start_round = pygame.mixer.Sound("assets/sounds/COD_start_round.mp3")
    start_round.set_volume(0.1)
    start_round.play()
    pygame.display.set_caption("Play")
    mixer.music.load('assets/sounds/ambient/ambience.mp3')
    mixer.music.set_volume(0.1)
    mixer.music.play(-1)
    main_menu_music.stop()

    while True:

        esc_key = pygame.key.get_pressed()
        for i in range(int(height / bg_size_y)):
            for j in range(int(width / bg_size_x)):
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

        # player.movement(col(player, [player, player2] + zombie + [Background[5][5]]))
        # player2.movement(col(player2, [player, player2] + zombie + [Background[5][5]]))

        pygame.time.delay(15)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if esc_key[pygame.K_ESCAPE]:
                start_round.stop()
                mixer.music.pause()
                pause()


def main_menu():
    main_menu_music.play()

    while True:

        menu_mouse_pos = pygame.mouse.get_pos()
        screen.blit(menu_BG, (0, 0))

        main_menu_button()

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
