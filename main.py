import sys
import pygame
from game_background import Background, get_font, menu_BG, esc_menu
from player import player, player2
from constants import width, height, bg_size_x, bg_size_y
from button import Button
from math import sqrt
from collision import col
from pygame import mixer
from enemy.zombie import zombie_group, zombie, zombie1, matrix
#from threading import Thread
from screen import screen


stop = True

pygame.init()
pygame.display.set_caption("POVT.EXE")
game_icon = programIcon = pygame.image.load('assets/images/game_icon.png')
pygame.display.set_icon(game_icon)
in_game_Background = Background

clock = pygame.time.Clock()

button_hover_state_yes = False
button_hover_state_no = False

button_click = pygame.mixer.Sound("assets/sounds/main_menu/button_click.mp3")
button_click.set_volume(0.3)

button_hover = pygame.mixer.Sound("assets/sounds/main_menu/button_hover.mp3")
button_hover.set_volume(0.2)

main_menu_music = pygame.mixer.Sound("assets/sounds/main_menu/main_menu_music.mp3")
main_menu_music.set_volume(0.08)

button_hover_state_solo = False
button_hover_state_duo = False
button_hover_state_exit = False


def pause():
    paused = True
    main_menu_music.play()
    global button_hover_state_yes, button_hover_state_no
    while paused:
        menu_mouse_pos = pygame.mouse.get_pos()

        yes_button = Button(image=pygame.image.load("assets/images/main_menu/button_yes.png"), pos=(250, 560),
                            text_input="Yes", font=get_font(32), base_color="White", hovering_color="#43f1f8")
        no_button = Button(image=pygame.image.load("assets/images/main_menu/button_no.png"), pos=(736, 560),
                           text_input="No", font=get_font(32), base_color="White", hovering_color="#679B00")

        current_hover_play_yes = 190 <= pygame.mouse.get_pos()[0] <= 316 and 518 <= pygame.mouse.get_pos()[
            1] <= 601
        current_hover_play_no = 680 <= pygame.mouse.get_pos()[0] <= 805 and 518 <= pygame.mouse.get_pos()[
            1] <= 601

        # Hover sound for play_yes
        if current_hover_play_yes and not button_hover_state_yes:
            button_hover.play(0)
            button_hover_state_yes = True
        elif not current_hover_play_yes and button_hover_state_yes:
            button_hover_state_yes = False
        # Hover sound for play_duo
        if current_hover_play_no and not button_hover_state_no:
            button_hover.play(0)
            button_hover_state_no = True
        elif not current_hover_play_no and button_hover_state_no:
            button_hover_state_no = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if yes_button.checkForInput(menu_mouse_pos):
                    button_click.play()
                    pygame.quit()
                    quit()
                if no_button.checkForInput(menu_mouse_pos):
                    button_click.play()
                    mixer.music.unpause()
                    main_menu_music.stop()
                    paused = False

        screen.blit(esc_menu, (0, 0))

        for button in [yes_button, no_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)

        pygame.display.update()
        clock.tick(50)


def play_solo():

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
        keko = clock.get_fps() # TODO: Поменяй
        pygame.display.set_caption("FPS: " + str(keko))
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

        player.movement(col(player, (zombie1, zombie, Background[5][5])))
        player.render_player()

        zombie.update()
        zombie.movement(matrix, col(zombie, (zombie1, zombie, player, Background[5][5])))
        zombie1.update()
        zombie1.movement(matrix, col(zombie1, (zombie1, zombie, player, Background[5][5])))
        zombie_group.draw(screen)

        bullets_list = player.shoot(bullets_list, [zombie, zombie1])
        # bullets_list, zombie_group = player.shoot(bullets_list, zombie_group)

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
                zombie.create_path(zombie.rect.x // 50, zombie.rect.y // 50, matrix, True, player.rect)
                zombie1.create_path(zombie1.rect.x // 50, zombie1.rect.y // 50, matrix, True, player.rect)
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

        """for i in zombie:
            i.render_zombie()

            if (not i.attack_player(player.rect)) and (not i.attack_player(player2.rect)):
                if dist(i):
                    pass
                   # i.move(player2.rect.x, player2.rect.y, col(i, zombie + [Background[5][5]]))
                else:
                    pass
                    #i.move(player.rect.x, player.rect.y, col(i, zombie + [Background[5][5]]))"""

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

