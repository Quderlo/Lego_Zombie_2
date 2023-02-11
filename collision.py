from constants import collision_tolerance, player_size
from math import sqrt


def zombie_collision(zombie, arr_zombie):
    blocked_side = {'top': False, 'bottom': False, 'left': False, 'right': False}
    for i in arr_zombie:
        if (int(sqrt((zombie.rect.x - i.rect.x) ** 2 + (zombie.rect.y - i.rect.y) ** 2)) <= player_size + 10)\
                and (zombie != i):
            if abs(zombie.rect.top - i.rect.bottom) <= collision_tolerance or blocked_side['top']:
                blocked_side['top'] = True
            else:
                blocked_side['top'] = False
            if abs(zombie.rect.bottom - i.rect.top) <= collision_tolerance or blocked_side['bottom']:
                blocked_side['bottom'] = True
            else:
                blocked_side['bottom'] = False
            if abs(zombie.rect.left - i.rect.right) <= collision_tolerance or blocked_side['left']:
                blocked_side['left'] = True
            else:
                blocked_side['left'] = False
            if abs(zombie.rect.right - i.rect.left) <= collision_tolerance or blocked_side['right']:
                blocked_side['right'] = True
            else:
                blocked_side['right'] = False
    return blocked_side




