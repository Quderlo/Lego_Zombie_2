from game_background import get_font, esc_menu
from main_menu_buttons import button_click, main_menu_music, button_hover
import pygame
from button import Button
from pygame import mixer
from screen import screen

clock = pygame.time.Clock()
button_hover_state_yes = False
button_hover_state_no = False


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

        # print(menu_mouse_pos)
        for button in [yes_button, no_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)

        pygame.display.update()
        clock.tick(50)
