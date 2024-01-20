import pygame
import math


def draw_minimap(screen, map_world, minimap_size, player_coord):
    len_map_s = len(map_world)
    len_map_r = len(map_world[0])
    for i in range(len_map_s):
        for j in range(len_map_r):
            if map_world[i][j]:
                pygame.draw.rect(screen, 'white', (i * minimap_size, j * minimap_size,
                                                   minimap_size, minimap_size))
            else:
                pygame.draw.rect(screen, 'black', (i * minimap_size, j * minimap_size,
                                                   minimap_size, minimap_size))

    pygame.draw.circle(screen, "white", player_coord, minimap_size / 5)
    pygame.draw.rect(screen, 'black', (0, 0, minimap_size * len_map_s, minimap_size * len_map_r), 2)
