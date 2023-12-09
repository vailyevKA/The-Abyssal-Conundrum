import pygame
import math


def draw_minimap(screen, map_world, minimap_size, player_coord):
    len_map = len(map_world)
    for i in range(len_map):
        for j in range(len_map):
            if map_world[i][j]:
                pygame.draw.rect(screen, "white", (i * minimap_size, j * minimap_size,
                                                   minimap_size, minimap_size))

    pygame.draw.circle(screen, "white", player_coord, minimap_size / 5)

    # x = player_coord[0] + math.cos(math.radians(angle)) * 1032
    # y = player_coord[1] + math.sin(math.radians(angle)) * 1032
    # pygame.draw.line(screen, "red", player_coord, (x, y), 2)
