import pygame
from constants import width, height, player_size, player_move_speed
from bullets import Bullet
from screen import screen

bool_for_timer = True

player1_x = width / 2 - player_size
player1_y = height / 2 - player_size
player2_x = width / 2 + player_size
player2_y = height / 2 - player_size


player1_texture = pygame.image.load('assets/images/player_img/player_up.jpg').convert()
player2_texture = pygame.image.load('assets/images/player2_img/player2_up.jpg').convert()

player1_texture_up = pygame.image.load('assets/images/player_img/player_up.jpg').convert()
player1_texture_down = pygame.image.load('assets/images/player_img/player_down.jpg').convert()
player1_texture_right = pygame.image.load('assets/images/player_img/player_right.jpg').convert()
player1_texture_left = pygame.image.load('assets/images/player_img/player_left.jpg').convert()
player1_texture_right_down = pygame.image.load('assets/images/player_img/player_right_down.jpg').convert()
player1_texture_up_right = pygame.image.load('assets/images/player_img/player_up_right.jpg').convert()
player1_texture_up_left = pygame.image.load('assets/images/player_img/player_up_left.jpg').convert()
player1_texture_down_left = pygame.image.load('assets/images/player_img/player_down_left.jpg').convert()

player2_texture_up = pygame.image.load('assets/images/player2_img/player2_up.jpg')
player2_texture_down = pygame.image.load('assets/images/player2_img/player2_down.jpg').convert()
player2_texture_right = pygame.image.load('assets/images/player2_img/player2_right.jpg').convert()
player2_texture_left = pygame.image.load('assets/images/player2_img/player2_left.jpg').convert()
player2_texture_right_down = pygame.image.load('assets/images/player2_img/player2_down_right.jpg').convert()
player2_texture_up_right = pygame.image.load('assets/images/player2_img/player2_up_right.jpg').convert()
player2_texture_up_left = pygame.image.load('assets/images/player2_img/player2_up_left.jpg').convert()
player2_texture_down_left = pygame.image.load('assets/images/player2_img/player2_down_left.jpg').convert()


class Player(object):
    def __init__(self, texture, px, py):
        img = texture
        self.image = pygame.transform.scale(img, (player_size, player_size))
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
        self.side = (0, -1)

    def move(self, diffx, diffy, blocked_side):
        if (not blocked_side['right'] and diffx > 0) or (not blocked_side['left'] and diffx < 0):
            self.rect.x += diffx
        if (not blocked_side['bottom'] and diffy > 0) or (not blocked_side['top'] and diffy < 0):
            self.rect.y += diffy

    def render_player(self):
        screen.blit(self.image, self.rect)

    def movement(self, blocked_side):
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN] and key[pygame.K_RIGHT] and not (self.rect.bottom >= height):
            self.image = player1_texture_right_down
            self.side = (player_move_speed, player_move_speed)
            self.move(self.side[0], self.side[1], blocked_side)

        elif key[pygame.K_UP] and key[pygame.K_RIGHT] and not (self.rect.bottom >= height):
            self.image = player1_texture_up_right
            self.side = (player_move_speed, -player_move_speed)
            self.move(self.side[0], self.side[1], blocked_side)

        elif key[pygame.K_UP] and key[pygame.K_LEFT] and not (self.rect.bottom >= height):
            self.image = player1_texture_up_left
            self.side = (-player_move_speed, -player_move_speed)
            self.move(self.side[0], self.side[1], blocked_side)

        elif key[pygame.K_DOWN] and key[pygame.K_LEFT] and not (self.rect.bottom >= height):
            self.image = player1_texture_down_left
            self.side = (-player_move_speed, player_move_speed)
            self.move(self.side[0], self.side[1], blocked_side)

        elif key[pygame.K_LEFT] and not(self.rect.left <= 0):
            self.image = player1_texture_left
            self.side = (-player_move_speed, 0)
            self.move(self.side[0], self.side[1], blocked_side)

        elif key[pygame.K_RIGHT] and not(self.rect.right >= width):
            self.image = player1_texture_right
            self.side = (player_move_speed, 0)
            self.move(self.side[0], self.side[1], blocked_side)

        elif key[pygame.K_UP] and not(self.rect.top <= 0):
            self.image = player1_texture_up
            self.side = (0, -player_move_speed)
            self.move(self.side[0], self.side[1], blocked_side)

        elif key[pygame.K_DOWN] and not(self.rect.bottom >= height):
            self.image = player1_texture_down
            self.side = (0, player_move_speed)
            self.move(self.side[0], self.side[1], blocked_side)

    def shoot(self, bullets_list):

        key = pygame.key.get_pressed()

        for bullet in bullets_list:
            if bullet.rect.x >= width or bullet.rect.x <= 0 \
                    or bullet.rect.y >= height or bullet.rect.y <= 0:
                bullets_list.pop(bullets_list.index(bullet))
            else:
                bullet.move()
                bullet.render()

        if key[pygame.K_SPACE]:
            bullets_list.append(Bullet(player))
        return bullets_list


class Player2(Player):
    def movement(self, blocked_side):
        key = pygame.key.get_pressed()

        if key[pygame.K_w] and key[pygame.K_a] and not(self.rect.left <= 0):
            self.image = player2_texture_up_left
            self.side = (-player_move_speed, -player_move_speed)
            self.move(self.side[0], self.side[1], blocked_side)

        elif key[pygame.K_w] and key[pygame.K_d] and not(self.rect.left <= 0):
            self.image = player2_texture_up_right
            self.side = (player_move_speed, -player_move_speed)
            self.move(self.side[0], self.side[1], blocked_side)

        elif key[pygame.K_s] and key[pygame.K_a] and not(self.rect.left <= 0):
            self.image = player2_texture_down_left
            self.side = (-player_move_speed, player_move_speed)
            self.move(self.side[0], self.side[1], blocked_side)

        elif key[pygame.K_s] and key[pygame.K_d] and not(self.rect.left <= 0):
            self.image = player2_texture_right_down
            self.side = (player_move_speed, player_move_speed)
            self.move(self.side[0], self.side[1], blocked_side)

        elif key[pygame.K_a] and not(self.rect.left <= 0):
            self.image = player2_texture_left
            self.side = (-player_move_speed, 0)
            self.move(self.side[0], self.side[1], blocked_side)

        elif key[pygame.K_d] and not(self.rect.right >= width):
            self.image = player2_texture_right
            self.side = (player_move_speed, 0)
            self.move(self.side[0], self.side[1], blocked_side)

        elif key[pygame.K_w] and not(self.rect.top <= 0):
            self.image = player2_texture_up
            self.side = (0, -player_move_speed)
            self.move(self.side[0], self.side[1], blocked_side)

        elif key[pygame.K_s] and not(self.rect.bottom >= height):
            self.image = player2_texture_down
            self.side = (0, player_move_speed)
            self.move(self.side[0], self.side[1], blocked_side)


player = Player(player1_texture, player1_x, player1_y)
player2 = Player2(player2_texture, player2_x, player2_y)
