from constants import collision_tolerance, player_size
from math import sqrt


def col(subject, arr_subject):
    blocked_side = {'top': False, 'bottom': False, 'left': False, 'right': False}
    for i in arr_subject:
        if (int(sqrt((subject.rect.x - i.rect.x) ** 2 + (subject.rect.y - i.rect.y) ** 2)) <= player_size + 10)\
                and (subject != i):
            if abs(subject.rect.top - i.rect.bottom) <= collision_tolerance or blocked_side['top']:
                blocked_side['top'] = True
            else:
                blocked_side['top'] = False
            if abs(subject.rect.bottom - i.rect.top) <= collision_tolerance or blocked_side['bottom']:
                blocked_side['bottom'] = True
            else:
                blocked_side['bottom'] = False
            if abs(subject.rect.left - i.rect.right) <= collision_tolerance or blocked_side['left']:
                blocked_side['left'] = True
            else:
                blocked_side['left'] = False
            if abs(subject.rect.right - i.rect.left) <= collision_tolerance or blocked_side['right']:
                blocked_side['right'] = True
            else:
                blocked_side['right'] = False
    return blocked_side




