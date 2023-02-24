import threading
from math import sqrt

from collision import col
from constants import player_size
from enemy.zombie import zombie, matrix
from game_background import bg_col
from player import player, player2
import time

bool_of_move = True


def dist(pos):
    zombie_to_player1_dist = int(sqrt((pos.rect.x - player.rect.x) ** 2 + (pos.rect.y - player.rect.y) ** 2))
    zombie_to_player2_dist = int(sqrt((pos.rect.x - player2.rect.x) ** 2 + (pos.rect.y - player2.rect.y) ** 2))
    return zombie_to_player1_dist < zombie_to_player2_dist


def enemy_path_ai():
    while True:
        time.sleep(1)
        for i in range(10):
            try:
                if dist(zombie[i]):
                    zombie[i].create_path(zombie[i].rect.x // 50, zombie[i].rect.y // 50, matrix, True, player.rect,
                                          col(zombie[i], zombie + [player, player2] + bg_col))
                else:
                    zombie[i].create_path(zombie[i].rect.x // 50, zombie[i].rect.y // 50, matrix, True, player2.rect,
                                          col(zombie[i], zombie + [player, player2] + bg_col))
            except:
                pass


def enemy_attack_one():
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

                player.hp -= 10  # TODO: enemy_damage
                time.sleep(0.5)

        bool_of_move = True


def enemy_attack_two():
    global bool_of_move

    while True:
        time.sleep(1)
        for i in range(len(zombie)):
            # zombie[i].self_distance(player)

            if zombie[i].self_distance(player2) <= 100:
                near_zombie = zombie[i]
                bool_of_move = False

                if near_zombie.rect.y // player_size < player2.rect.y // player_size:
                    for j in range(30):
                        player2.move(0, 2, col(player2, zombie + [player2] + bg_col))
                        time.sleep(0.0025)

                elif near_zombie.rect.y // player_size > player.rect.y // player_size:
                    for j in range(30):
                        player2.move(0, -2, col(player2, zombie + [player2] + bg_col))
                        time.sleep(0.0025)

                elif near_zombie.rect.x // player_size < player2.rect.x // player_size:
                    for j in range(30):
                        player2.move(2, 0, col(player2, zombie + [player2] + bg_col))
                        time.sleep(0.0025)

                elif near_zombie.rect.x // player_size > player2.rect.x // player_size:
                    for j in range(30):
                        player2.move(-2, 0, col(player2, zombie + [player2] + bg_col))
                        time.sleep(0.0025)

                player2.hp -= 10  # TODO: enemy_damage
                time.sleep(0.5)

        bool_of_move = True


t_enemy_attack_two = threading.Thread(target=enemy_attack_one, daemon=True)
t_enemy_attack_one = threading.Thread(target=enemy_attack_two, daemon=True)
t_create_path = threading.Thread(target=enemy_path_ai, daemon=True)
