import math
from settings import *


def can_go(player_x, player_y, angle, is_ahead, speed):
    if is_ahead:
        next_x = player_x + (minimap_size / 30) * (math.cos(math.radians(angle))) * speed
        next_y = player_y + (minimap_size / 30) * (math.sin(math.radians(angle))) * speed
    else:
        next_x = player_x - (minimap_size / 30) * (math.cos(math.radians(angle))) * speed
        next_y = player_y - (minimap_size / 30) * (math.sin(math.radians(angle))) * speed

    if map_world[int(next_x // minimap_size)][int(next_y // minimap_size)]:
        return False
    return True