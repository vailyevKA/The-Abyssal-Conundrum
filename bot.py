from settings import bot_coord, minimap_size, bot_angle
import pygame
from raycasting import ray_casting_bot


def bot_paint(display):
    pygame.draw.circle(display, "white", bot_coord, minimap_size / 5)

    ray_casting_bot(display, bot_coord, bot_angle, 90)
    ray_casting_bot(display, bot_coord, bot_angle + 45, 90)
    ray_casting_bot(display, bot_coord, bot_angle + 60, 90)
    ray_casting_bot(display, bot_coord, bot_angle + 30, 90)
