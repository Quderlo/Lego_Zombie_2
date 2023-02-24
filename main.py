import sys
import threading
import time

import pygame

from enemy.ai import t_enemy_attack_one, t_enemy_attack_two, t_create_path, bool_of_move, dist
from game_background import Background, get_font, menu_BG, esc_menu
from main_menu_buttons import main_menu_music, button_click, main_menu_button, game_over_music
from player import player, player2
from constants import width, height, bg_size_x, bg_size_y
from button import Button
from math import sqrt
from collision import col
from pygame import mixer
from enemy.zombie import zombie, matrix, num_of_enemies, t_spawner
# from threading import Thread
from screen import screen
from pause import pause
from game_background import bg_col

pygame.init()
pygame.display.set_caption("POVT.EXE")
game_icon = programIcon = pygame.image.load('assets/images/game_icon.png')
pygame.display.set_icon(game_icon)
in_game_Background = Background
clock = pygame.time.Clock()


def game_over():
    game_is_over = True
    game_over_music.play()
    mixer.music.stop()
    menu = pygame.image.load('assets/images/main_menu/game_over.jpg')
    while game_is_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        screen.blit(menu, (0, 0))

        pygame.display.update()
        clock.tick(50)


def play_solo():

    player2.rect.x = 2000
    player2.rect.y = 2000

    t_spawner.start()
    t_enemy_attack_one.start()
    t_enemy_attack_two.start()
    t_create_path.start()

    player2.hp = 0


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
        our_hp = player.hp + player2.hp  # TODO: не допускать минусового hp
        if our_hp <= 0:
            game_over()

        get_fps = clock.get_fps()
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
            for j in range(10, count_now):
                if dist(zombie[j]):
                    zombie[j].stupid_ai(player.rect, col(zombie[j], zombie + [player, player2] + bg_col))
                else:
                    zombie[j].stupid_ai(player2.rect, col(zombie[j], zombie + [player, player2] + bg_col))

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


def play_duo():
    t_spawner.start()
    t_enemy_attack_one.start()
    t_enemy_attack_two.start()
    t_create_path.start()

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
        our_hp = player.hp + player2.hp  # TODO: не допускать минусового hp
        if our_hp <= 0:
            game_over()

        get_fps = clock.get_fps()
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

        get_fps = clock.get_fps()  # TODO: Поменяй       #TODO: это удалим потом
        pygame.display.set_caption("FPS: " + str(get_fps))
        try:
            for i in range(num_of_enemies):
                zombie[i].update()
                zombie[i].movement(matrix, col(zombie[i], zombie + [player, player2] + bg_col), bool_of_move)
        except:
            pass

        count_now = len(zombie)
        if count_now >= 10:
            for j in range(10, count_now):
                if dist(zombie[j]):
                    zombie[j].stupid_ai(player.rect, col(zombie[j], zombie + [player, player2] + bg_col))
                else:
                    zombie[j].stupid_ai(player2.rect, col(zombie[j], zombie + [player, player2] + bg_col))


        player.render_player()
        player2.render_player()

        player.movement(col(player, zombie + bg_col + [player2]))
        player2.movement(col(player2, [player] + zombie + bg_col))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if esc_key[pygame.K_ESCAPE]:
                start_round.stop()
                mixer.music.pause()
                pause()
        clock.tick(60)


def main_menu():
    main_menu_music.play()

    try:
        t_spawner.join()
        t_enemy_attack_one.join()
        t_enemy_attack_two.join()
        t_create_path.join()
    except:
        pass

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
