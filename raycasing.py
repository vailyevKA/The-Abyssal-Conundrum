import pygame
from settings import *

def ray_casting(screen, pos, angel):
    cur_angel = math.radians(angel) - HALF_FOV + DELTA_ANGLE / 2
    x1, y1 = pos
    for i in range(NUM_RAYS):
        sin_a = math.sin(cur_angel)
        cos_a = math.cos(cur_angel)
        for j in range(MAX_DEPTH):
            x = x1 + j * cos_a
            y = y1 + j * sin_a
            # x = x1 + math.cos(math.radians(cur_angel)) * 1032
            # y = y1 + math.cos(math.radians(cur_angel)) * 1032
            pygame.draw.line(screen, 'gray', player_coord, (x, y))
        cur_angel += DELTA_ANGLE
