import sys
import pygame


from game_background import Background, get_font, menu_BG, esc_menu
from main_menu_buttons import main_menu_music, button_click, main_menu_button, button_hover
from player import player, player2
from constants import width, height, bg_size_x, bg_size_y
from button import Button
from math import sqrt
from collision import col
from pygame import mixer
from enemy.zombie import zombie_group, zombie, zombie1, matrix
#from threading import Thread
from screen import screen
from pause import pause


pygame.init()
pygame.display.set_caption("POVT.EXE")
game_icon = programIcon = pygame.image.load('assets/images/game_icon.png')
pygame.display.set_icon(game_icon)
in_game_Background = Background
clock = pygame.time.Clock()


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

