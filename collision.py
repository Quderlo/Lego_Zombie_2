import pygame
from constants import collision_tolerance, player_size
from math import sqrt


def zombie_collision(zombie, arr_zombie):
    blocked_side = {'top': False, 'bottom': False, 'left': False, 'right': False}
    for i in arr_zombie:
        entry = 0
        if (int(sqrt((zombie.rect.x - zombie.rect.x) ** 2 + (i.rect.y - i.rect.y) ** 2)) <= player_size) and (zombie != i):
            if (abs(zombie.rect.top - i.rect.bottom) <= collision_tolerance) or ((blocked_side['top'] == True) and (entry >= 1)):
                blocked_side['top'] = True
            else:
                blocked_side['top'] = False
            if (abs(zombie.rect.bottom - i.rect.top) <= collision_tolerance) or ((blocked_side['bottom'] == True) and (entry >= 1)):
                blocked_side['bottom'] = True
            else:
                blocked_side['bottom'] = False
            if (abs(zombie.rect.left - i.rect.right) <= collision_tolerance) or ((blocked_side['left'] == True) and (entry >= 1)):
                blocked_side['left'] = True
            else:
                blocked_side['left'] = False
            if (abs(zombie.rect.right - i.rect.left) <= collision_tolerance) or ((blocked_side['right'] == True) and (entry >= 1)):
                blocked_side['right'] = True
            else:
                blocked_side['right'] = False
            if pygame.Rect.colliderect(zombie.rect, i.rect):
                blocked_side = {'top': True, 'bottom': True, 'left': True, 'right': True}

            entry += 1

    return blocked_side





