import time
import pygame
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import random
from threading import Thread
from constants import enemy_move_speed
from math import sqrt


# spawn enemy
coord_x = random.randint(100, 500)
coord_y = random.randint(100, 500)

const = 50

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()




matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]]


bool_for_timer = True


def timer():
    global bool_for_timer
    while True:
        bool_for_timer = False
        time.sleep(0.5)
        bool_for_timer = True


t = Thread(target=timer, args=(), daemon=True)
t.start()


class Enemy(object):
    enemy_count = 0
    enemy_hp = 110
    enemy_damage = 30

    def __init__(self, x, y):
        # basic
        self.image = pygame.image.load('assets/images/zombie_img/zombie_down.jpg').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # setup

        self.grid = Grid(matrix=matrix)

        # pathfinding
        self.path = []

    def self_distance(self, player):
        distance = int(sqrt((self.rect.x - player.rect.x) ** 2 + (self.rect.y - player.rect.y) ** 2))
        return distance

    def create_path(self, rect_x, rect_y, get, off_create_path, player_pos, blocked_side):
        # start

        if off_create_path:
            new_matrix = get
            self.grid = Grid(matrix=new_matrix)

            bypass = 2

            # bybass top
            if blocked_side['top'] and self.rect.x > player_pos[0]:
                rect_x -= bypass
                rect_y += bypass
            elif blocked_side['top'] and self.rect.x == player_pos[0]:
                rect_x -= bypass
                rect_y += bypass
            elif blocked_side['top'] and self.rect.x < player_pos[0]:
                rect_x += bypass
                rect_y += bypass



            # bybass bottom
            elif blocked_side['bottom'] and self.rect.x > player_pos[0]:
                rect_x -= bypass
                rect_y -= bypass
            elif blocked_side['bottom'] and self.rect.x < player_pos[0]:
                rect_x += bypass
                rect_y -= bypass

            # bypass right
            elif blocked_side['right'] and self.rect.y > player_pos[1]:
                rect_x -= bypass
                rect_y -= bypass
            elif blocked_side['right'] and self.rect.y < player_pos[1]:
                rect_y += bypass
                rect_x -= bypass

            # bypass left
            elif blocked_side['left'] and self.rect.y > player_pos[1]:
                rect_x -= bypass
                rect_y += bypass
            elif blocked_side['left'] and self.rect.y < player_pos[1]:
                rect_y -= bypass
                rect_x -= bypass

            start_x, start_y = rect_x, rect_y

            start = self.grid.node(start_x, start_y)

            # end
            end_x, end_y = player_pos[0] // const, player_pos[1] // const
            end = self.grid.node(end_x, end_y)

            # path
            finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
            self.path, _ = finder.find_path(start, end, self.grid)
            self.grid.cleanup()

            # path
            finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
            self.path, _ = finder.find_path(start, end, self.grid)
            self.grid.cleanup()


    def move(self, diffx, diffy, blocked_side):
        if (not blocked_side['right'] and diffx > 0) or (not blocked_side['left'] and diffx < 0):
            self.rect.x += diffx
        if (not blocked_side['bottom'] and diffy > 0) or (not blocked_side['top'] and diffy < 0):
            self.rect.y += diffy

    def movement(self, matrix_matrix, blocked_side, bool_of_move):
        global bool_for_timer

        id(matrix_matrix)

        # attack object

        #if blocked_side['bottom'] and player.rect.y > self.rect.y:
           # self.attack()
        if bool_of_move:
            # default move
            if len(self.path) != 0:
                xx = self.path[0][0]
                yy = self.path[0][1]
                # move right

                if self.rect.x // const < xx:
                    self.image = pygame.image.load('assets/images/zombie_img/zombie_right.jpg').convert_alpha()
                    self.move(enemy_move_speed, 0, blocked_side)
                # move left
                if self.rect.x // const > xx:
                    self.image = pygame.image.load('assets/images/zombie_img/zombie_left.jpg').convert_alpha()
                    self.move(-enemy_move_speed, 0, blocked_side)
                # move down
                if self.rect.y // const < yy:
                    self.image = pygame.image.load('assets/images/zombie_img/zombie_down.jpg').convert_alpha()
                    self.move(0, enemy_move_speed, blocked_side)
                # move up
                if self.rect.y // const > yy:
                    self.image = pygame.image.load('assets/images/zombie_img/zombie_up.jpg').convert_alpha()
                    self.move(0, -enemy_move_speed, blocked_side)

                # down right
                if (self.rect.x // const < xx) and (self.rect.y // const < yy):
                    self.image = pygame.image.load('assets/images/zombie_img/zombie_down_right.jpg').convert_alpha()
                # up right
                if (self.rect.x // const < xx) and (self.rect.y // const > yy):
                    self.image = pygame.image.load('assets/images/zombie_img/zombie_up_right.jpg').convert_alpha()
                # up left
                if (self.rect.x // const > xx) and (self.rect.y // const > yy):
                    self.image = pygame.image.load('assets/images/zombie_img/zombie_up_left.jpg').convert_alpha()
                # down left
                if (self.rect.x // const > xx) and (self.rect.y // const < yy):
                    self.image = pygame.image.load('assets/images/zombie_img/zombie_down_left.jpg').convert_alpha()
                if (self.rect.x // const == xx) and (self.rect.y // const == yy):
                    # print("DELETE")
                    self.path.pop(0)

    def stupid_ai(self, player, blocked_side):
        if player[0] > self.rect.x:
            self.move(enemy_move_speed - 1, 0, blocked_side)
        if player[1] > self.rect.y:
            self.move(0, enemy_move_speed - 1, blocked_side)
        if player[0] < self.rect.x:
            self.move(-enemy_move_speed + 1, 0, blocked_side)
        if player[1] < self.rect.y:
            self.move(0, -enemy_move_speed + 1, blocked_side)

    def draw_path(self):
        if self.path:
            points = []
            for point in self.path:
                x = (point[0] * const) + const / 2
                y = (point[1] * const) + const / 2
                points.append((x, y))
            try:
                pygame.draw.lines(screen, '#34c924', False, points, 5)
            except:
                pass
                #print("error")

    def update(self):
        self.draw_path()
        screen.blit(self.image, self.rect)


pygame.time.set_timer(pygame.USEREVENT, 500)

zombie = []

num_of_enemies = 30 // 2

spawn = True


def spawner(count):
    count_now = 0

    while count > count_now:
        count_now = len(zombie)
        z = Enemy(random.randint(450, 500), random.randint(0, 0))
        z1 = Enemy(random.randint(450, 500), random.randint(990, 1000))
        zombie.append(z)
        zombie.append(z1)
        time.sleep(3)


t2 = Thread(target=spawner, args=(num_of_enemies,), daemon=True)





