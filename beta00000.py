import pygame
from pygame.locals import *
import sys
import math
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Raycasting Game")
black = (0, 0, 0)
white = (255, 255, 255)
player_x = 100
player_y = 100
player_angle = 0
map_resolution = 50
level_map = [
    "111111111111",
    "100000000001",
    "100001000001",
    "100001000001",
    "100000000001",
    "100011000001",
    "111111111111"
]


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[K_LEFT]:
        player_angle -= 0.2
    if keys[K_RIGHT]:
        player_angle += 0.2
    if keys[K_UP]:
        player_x += 10 * math.cos(player_angle)
        player_y += 10 * math.sin(player_angle)
    if keys[K_DOWN]:
        player_x -= 10 * math.cos(player_angle)
        player_y -= 10 * math.sin(player_angle)


    screen.fill(black)

    for x in range(screen_width):
        ray_angle = (player_angle - math.pi / 6) + (x / screen_width) * (math.pi / 3)

        distance_to_wall = 0
        hit_wall = False

        eye_x = player_x
        eye_y = player_y

        while not hit_wall and distance_to_wall < 800:
            distance_to_wall += 1
            test_x = int(eye_x + distance_to_wall * math.cos(ray_angle))
            test_y = int(eye_y + distance_to_wall * math.sin(ray_angle))

            if level_map[test_y // map_resolution][test_x // map_resolution] == "1":
                hit_wall = True

        wall_height = (map_resolution / distance_to_wall) * screen_height
        wall_color = (255, 255, 255)

        for y in range(int((screen_height - wall_height) / 2), int((screen_height + wall_height) / 2)):
            if 0 <= x < screen_width and 0 <= y < screen_height:
                screen.set_at((x, y), wall_color)

    pygame.draw.circle(screen, white, (int(player_x), int(player_y)), 5)
    pygame.display.flip()
    pygame.time.Clock().tick(10000)