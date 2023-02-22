import threading

from collision import col
from constants import player_size
from enemy.zombie import zombie, matrix
from game_background import bg_col
from player import player
import time

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
        time.sleep(1)
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


thr2 = threading.Thread(target=enemy_attack, daemon=True)
thr1 = threading.Thread(target=enemy_path_ai, daemon=True)

