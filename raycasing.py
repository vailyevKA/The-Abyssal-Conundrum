import pygame
from settings import *


def ray_casting(screen, pos, angle):
    cur_angle = math.radians(angle) - HALF_FOV + DELTA_ANGLE / 2
    x1, y1 = pos
    dist = 0
    for i in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for j in range(MAX_DEPTH):
            x = x1 + j * cos_a
            y = y1 + j * sin_a
            dist = ((x - x1)**2 + (y - y1)**2) ** 0.5
            pygame.draw.line(screen, 'gray', player_coord, (x, y))
            try:
                if map_world[int(x // minimap_size)][int(y // minimap_size)] == 1:
                    break
            except IndexError:
                continue
        height_rect = int((WALLS_SIZE / dist) * HEIGHT)
        width_rect = WIDTH / NUM_RAYS
        r = (256 - dist) % 256
        g = (256 - dist) % 256
        b = (256 - dist) % 256
        pygame.draw.rect(screen, (r, g, b), (i * width_rect, (HEIGHT - height_rect) / 2, width_rect + 1, height_rect))

        cur_angle += DELTA_ANGLE
        angle %= 360
        cur_angle %= 6.28
