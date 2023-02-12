import pygame
from constants import width, height, player_size, player_move_speed


pygame.init()

screen = pygame.display.set_mode((width, height))

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

    def move(self, diffx, diffy, blocked_side):
        if (not blocked_side['right'] and diffx > 0) or (not blocked_side['left'] and diffx < 0):
            self.rect.x += diffx
        if (not blocked_side['bottom'] and diffy > 0) or (not blocked_side['top'] and diffy < 0):
            self.rect.y += diffy

    def render_player(self):
        screen.blit(self.image, self.rect)

    def movement(self, blocked_side):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and not(self.rect.left <= 0):
            self.move(-player_move_speed, 0, blocked_side)
            self.image = player1_texture_left
        if key[pygame.K_RIGHT] and not(self.rect.right >= width):
            self.move(player_move_speed, 0, blocked_side)
            self.image = player1_texture_right
        if key[pygame.K_UP] and not(self.rect.top <= 0):
            self.move(0, -player_move_speed, blocked_side)
            self.image = player1_texture_up
        if key[pygame.K_DOWN] and not(self.rect.bottom >= height):
            self.move(0, player_move_speed, blocked_side)
            self.image = player1_texture_down

        if key[pygame.K_DOWN] and key[pygame.K_RIGHT] and not (self.rect.bottom >= height):
            self.image = player1_texture_right_down
        if key[pygame.K_UP] and key[pygame.K_RIGHT] and not (self.rect.bottom >= height):
            self.image = player1_texture_up_right
        if key[pygame.K_UP] and key[pygame.K_LEFT] and not (self.rect.bottom >= height):
            self.image = player1_texture_up_left
        if key[pygame.K_DOWN] and key[pygame.K_LEFT] and not (self.rect.bottom >= height):
            self.image = player1_texture_down_left


class Player2(Player):
    def movement(self, blocked_side):
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and not(self.rect.left <= 0):
            self.move(-player_move_speed, 0, blocked_side)
            self.image = player2_texture_left
        if key[pygame.K_d] and not(self.rect.right >= width):
            self.move(player_move_speed, 0, blocked_side)
            self.image = player2_texture_right
        if key[pygame.K_w] and not(self.rect.top <= 0):
            self.move(0, -player_move_speed, blocked_side)
            self.image = player2_texture_up
        if key[pygame.K_s] and not(self.rect.bottom >= height):
            self.move(0, player_move_speed, blocked_side)
            self.image = player2_texture_down

        if key[pygame.K_w] and key[pygame.K_a] and not(self.rect.left <= 0):
            self.image = player2_texture_up_left
        if key[pygame.K_w] and key[pygame.K_d] and not(self.rect.left <= 0):
            self.image = player2_texture_up_right
        if key[pygame.K_s] and key[pygame.K_a] and not(self.rect.left <= 0):
            self.image = player2_texture_down_left
        if key[pygame.K_s] and key[pygame.K_d] and not(self.rect.left <= 0):
            self.image = player2_texture_right_down


player = Player(player1_texture, player1_x, player1_y)
player2 = Player2(player2_texture, player2_x, player2_y)
