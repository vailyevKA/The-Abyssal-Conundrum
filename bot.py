import random

from settings import *
from game import *
import pygame


def find_target():
    x_r, y_r = bot_coord
    x_l, y_l = bot_coord
    x_u, y_u = bot_coord
    x_d, y_d = bot_coord
    ways = ("right", "left", "up", "down")
    way = random.choice(ways)

    # right
    while not (map_world[int(x_r // minimap_size)][int(y_r // minimap_size)]):
        x_r += minimap_size

    # left
    while not (map_world[int(x_l // minimap_size)][int(y_l // minimap_size)]):
        x_l -= minimap_size

    # up
    while not (map_world[int(x_u // minimap_size)][int(y_u // minimap_size)]):
        y_u += minimap_size

    # down
    while not (map_world[int(x_d // minimap_size)][int(y_d // minimap_size)]):
        y_d -= minimap_size

    if way == "right":
        return x_r - minimap_size, y_r, way

    if way == "left":
        return x_l + minimap_size, y_l, way

    if way == "up":
        return x_u, y_u - minimap_size, way

    if way == "down":
        return x_d, y_d + minimap_size, way


def is_bot_see_player():
    player_coord_in_map = [int(player_coord[0] // minimap_size), int(player_coord[1] // minimap_size)]
    x_r, y_r = bot_coord
    x_l, y_l = bot_coord
    x_u, y_u = bot_coord
    x_d, y_d = bot_coord

    # right
    way = "right"
    while not (map_world[int(x_r // minimap_size)][int(y_r // minimap_size)]):
        x_r += minimap_size
        if list((int(x_r // minimap_size), int(y_r // minimap_size))) == player_coord_in_map:
            return x_r, y_r, way

    # left
    way = "left"
    while not (map_world[int(x_l // minimap_size)][int(y_l // minimap_size)]):
        x_l -= minimap_size
        if list((int(x_l // minimap_size), int(y_l // minimap_size))) == player_coord_in_map:
            return x_l, y_l, way

    # up
    way = "up"
    while not (map_world[int(x_u // minimap_size)][int(y_u // minimap_size)]):
        y_u += minimap_size
        if list((int(x_u // minimap_size), int(y_u // minimap_size))) == player_coord_in_map:
            return x_u, y_u, way

    # down
    way = "down"
    while not (map_world[int(x_d // minimap_size)][int(y_d // minimap_size)]):
        y_d -= minimap_size
        if list((int(x_d // minimap_size), int(y_d // minimap_size))) == player_coord_in_map:
            return x_d, y_d, way

    return False, False, False


def draw_monster(surface, center, scale):
    colors = {
        'dark_brown': (101, 67, 33),
        'light_brown': (160, 82, 45),
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        'red': (255, 0, 0)
    }

    square_size = 1 * scale  # Larger squares for more detail
    bear_height_in_squares = 14  # The bear's height in squares
    bear_width_in_squares = 18  # The bear's width in squares, adjust if needed

    # Calculate the top left position based on the center position
    top_left_x = center[0] - (bear_width_in_squares * square_size) // 2
    top_left_y = center[1] - (bear_height_in_squares * square_size) // 2

    # Body parts - each tuple represents a square (x, y, color)
    body = [
        # Head
        (10, 5, 'dark_brown'), (11, 5, 'dark_brown'), (12, 5, 'dark_brown'), (13, 5, 'dark_brown'),
        (14, 5, 'dark_brown'),
        (9, 6, 'dark_brown'), (10, 6, 'light_brown'), (11, 6, 'light_brown'), (12, 6, 'light_brown'),
        (13, 6, 'light_brown'), (14, 6, 'light_brown'), (15, 6, 'dark_brown'),
        (9, 7, 'dark_brown'), (10, 7, 'light_brown'), (11, 7, 'light_brown'), (12, 7, 'light_brown'),
        (13, 7, 'light_brown'), (14, 7, 'light_brown'), (15, 7, 'dark_brown'),
        (10, 8, 'dark_brown'), (11, 8, 'light_brown'), (12, 8, 'light_brown'), (13, 8, 'light_brown'),
        (14, 8, 'dark_brown'),
        (11, 9, 'dark_brown'), (12, 9, 'dark_brown'), (13, 9, 'dark_brown'),

        # Body
        (11, 10, 'light_brown'), (12, 10, 'light_brown'), (13, 10, 'light_brown'),
        (11, 11, 'light_brown'), (12, 11, 'light_brown'), (13, 11, 'light_brown'),
        (11, 12, 'light_brown'), (12, 12, 'light_brown'), (13, 12, 'light_brown'),

        # Arms
        (8, 10, 'light_brown'), (9, 10, 'light_brown'),
        (8, 11, 'light_brown'), (9, 11, 'light_brown'),
        (15, 10, 'light_brown'), (16, 10, 'light_brown'),
        (15, 11, 'light_brown'), (16, 11, 'light_brown'),

        # Legs
        (10, 13, 'light_brown'), (11, 13, 'light_brown'),
        (12, 13, 'light_brown'), (13, 13, 'light_brown'),
        (10, 14, 'light_brown'), (11, 14, 'light_brown'),
        (12, 14, 'light_brown'), (13, 14, 'light_brown'),

        # Ears
        (8, 4, 'dark_brown'), (9, 4, 'dark_brown'),
        (15, 4, 'dark_brown'), (16, 4, 'dark_brown'),

        # Eyes
        (10, 6, 'black'), (13, 6, 'black'),

        # Nose
        (12, 8, 'black'),

        # Mouth
        (12, 9, 'red')
    ]

    for x, y, color in body:
        pygame.draw.rect(surface, colors[color],
                         (top_left_x + x * square_size, top_left_y + y * square_size, square_size, square_size))




