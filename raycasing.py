import math
import pygame
from settings import *


def ray_casting(screen, pos, angle):
    cur_angle = math.radians(angle) - HALF_FOV + DELTA_ANGLE / 2
    x1, y1 = pos
    dist = 0
    for i in range(NUM_RAYS):
        wall = 0
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for j in range(MAX_DEPTH):
            x = x1 + j * cos_a
            y = y1 + j * sin_a
            dist = ((x - x1)**2 + (y - y1)**2) ** 0.5
            pygame.draw.line(screen, 'gray', player_coord, (x, y))
            try:
                wall = map_world[int(x // minimap_size)][int(y // minimap_size)]
                if wall:
                    break
            except IndexError:
                continue

        height_rect = int((WALLS_SIZE / dist) * HEIGHT)
        width_rect = WIDTH / NUM_RAYS
        if wall == 1:
            r = (255 - dist) % 255
            g = (255 - dist) % 255
            b = (255 - dist) % 255

        else:
            r = (153 - dist) % 255
            g = (102 - dist) % 255
            b = (204 - dist) % 255

        pygame.draw.rect(screen, (r, g, b),
                         (i * width_rect, (HEIGHT - height_rect) / 2, width_rect + 1, height_rect))

        cur_angle += DELTA_ANGLE
        angle %= 360
        cur_angle %= 6.28


def ray_casting_bot(screen, pos, angle, delta):
    cur_angle = math.radians(angle)
    x1, y1 = pos
    for i in range(4):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for j in range(MAX_DEPTH):
            x = x1 + j * cos_a
            y = y1 + j * sin_a
            pygame.draw.line(screen, 'gray', bot_coord, (x, y))
            try:
                wall = map_world[int(x // minimap_size)][int(y // minimap_size)]
                if wall:
                    break
            except IndexError:
                continue

        cur_angle += math.radians(delta)
