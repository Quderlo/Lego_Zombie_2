import pygame



button_hover_state_solo = False
button_hover_state_duo = False
button_hover_state_exit = False

button_click = pygame.mixer.Sound("assets/sounds/main_menu/button_click.mp3")
button_click.set_volume(0.3)

button_hover = pygame.mixer.Sound("assets/sounds/main_menu/button_hover.mp3")
button_hover.set_volume(0.2)

main_menu_music = pygame.mixer.Sound("assets/sounds/main_menu/main_menu_music.mp3")
main_menu_music.set_volume(0.08)

def main_menu_button():
    global button_hover_state_solo, button_hover_state_duo, button_hover_state_exit

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

