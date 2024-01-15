import random

from settings import *
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
