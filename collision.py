import pygame

from constants import collision_tolerance, player_size
from math import sqrt


def col(subject, arr_subject):
    blocked_side = {'top': False, 'bottom': False, 'left': False, 'right': False}

    for i in arr_subject:
        if subject != i:
            subject_width = subject.rect.topright[0] - subject.rect.topleft[0]
            subject_height = subject.rect.bottomright[1] - subject.rect.topright[1]

            i_width = i.rect.topright[0] - i.rect.topleft[0]
            i_height = i.rect.bottomright[1] - i.rect.topright[1]

            if abs(subject.rect.centerx - i.rect.centerx) <= (subject_width + i_width) \
                    and abs(subject.rect.centery - i.rect.centery) <= (subject_height + i_height):

                if abs(subject.rect.left - i.rect.left) + abs(subject.rect.right - i.rect.right) <= \
                        (int(subject_height + i_height) + collision_tolerance):

                    if (abs(subject.rect.top - i.rect.bottom) <= collision_tolerance or blocked_side['top']
                            or abs(subject.rect.topleft[1] - i.rect.bottomleft[1]) <= collision_tolerance
                            or abs(subject.rect.topright[1] - i.rect.bottomright[1]) <= collision_tolerance):
                        blocked_side['top'] = True
                    else:
                        blocked_side['top'] = False

                    if (abs(subject.rect.bottom - i.rect.top) <= collision_tolerance or blocked_side['bottom']
                            or abs(subject.rect.bottomleft[1] - i.rect.topleft[1]) <= collision_tolerance
                            or abs(subject.rect.bottomright[1] - i.rect.topright[1]) <= collision_tolerance):
                        blocked_side['bottom'] = True
                    else:
                        blocked_side['bottom'] = False

                if abs(subject.rect.top - i.rect.top) + abs(subject.rect.bottom - i.rect.bottom) <= \
                        (int(subject_width + i_width) + collision_tolerance):

                    if (abs(subject.rect.left - i.rect.right) <= collision_tolerance or blocked_side['left']
                            or abs(subject.rect.bottomleft[0] - i.rect.bottomright[0]) <= collision_tolerance
                            or abs(subject.rect.topleft[0] - i.rect.topright[0]) <= collision_tolerance):
                        blocked_side['left'] = True
                    else:
                        blocked_side['left'] = False

                    if (abs(subject.rect.right - i.rect.left) <= collision_tolerance or blocked_side['right']
                            or abs(subject.rect.bottomright[0] - i.rect.bottomleft[0]) <= collision_tolerance
                            or abs(subject.rect.topright[0] - i.rect.topleft[0]) <= collision_tolerance):
                        blocked_side['right'] = True
                    else:
                        blocked_side['right'] = False

    return blocked_side
