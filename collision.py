import pygame
from constants import collision_tolerance


def zombie_collision(zombie, arr_zombie):
    blocked_side = {'top': False, 'bottom': False, 'left': False, 'right': False}
    for i in arr_zombie:
        if abs(((zombie.rect.x + zombie.rect.y) - (i.rect.x + i.rect.y)) <= 200) and (zombie != i):
            if abs(zombie.rect.top - i.rect.bottom) < collision_tolerance:
                blocked_side['top'] = True
            else:
                blocked_side['top'] = False
            if abs(zombie.rect.bottom - i.rect.top) < collision_tolerance:
                blocked_side['bottom'] = True
            else:
                blocked_side['bottom'] = False
            if abs(zombie.rect.left - i.rect.right) < collision_tolerance:
                blocked_side['left'] = True
            else:
                blocked_side['left'] = False
            if abs(zombie.rect.right - i.rect.left) < collision_tolerance:
                blocked_side['right'] = True
            else:
                blocked_side['right'] = False

            print(blocked_side)
            return blocked_side




