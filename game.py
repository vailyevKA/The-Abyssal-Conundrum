import pygame
import sys
import math
from settings import *

if __name__ == '__main__':
    # Инициализация Pygame
    pygame.init()

    # Создание окна
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Моя игра на Pygame")

    # Инициализация переменных времени и FPS
    clock = pygame.time.Clock()
    FPS = 60

    running = True

    mot_w = False
    mot_s = False
    mot_d = False
    mot_a = False

    rot_r = False
    rot_l = False

    angle = 180

    # Основной игровой цикл

    while running:
        screen.fill("black")

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    mot_w = True

                if event.key == pygame.K_s:
                    mot_s = True

                if event.key == pygame.K_d:
                    rot_r = True

                if event.key == pygame.K_a:
                    rot_l = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    mot_w = False

                if event.key == pygame.K_s:
                    mot_s = False

                if event.key == pygame.K_d:
                    rot_r = False

                if event.key == pygame.K_a:
                    rot_l = False

        if mot_w:
            player_coord[0] += (minimap_size / 30) * (player_coord[0] - player_coord[0] + math.cos(math.radians(angle)))
            player_coord[1] += (minimap_size / 30) * (player_coord[1] - player_coord[1] + math.sin(math.radians(angle)))

        if mot_s:
            player_coord[0] -= (minimap_size / 30) * (player_coord[0] - player_coord[0] + math.cos(math.radians(angle)))
            player_coord[1] -= (minimap_size / 30) * (player_coord[1] - player_coord[1] + math.sin(math.radians(angle)))

        if rot_r:
            angle += mouse_speed
            angle %= 360

        if rot_l:
            angle -= mouse_speed
            angle %= 360

        # отрисовка миникарты

        len_map = len(map_world)
        for i in range(len_map):
            for j in range(len_map):
                if map_world[i][j]:
                    pygame.draw.rect(screen, "white", (i * minimap_size, j * minimap_size,
                                     minimap_size, minimap_size))

        pygame.draw.circle(screen, "white", player_coord, minimap_size / 5)

        x = player_coord[0] + math.cos(math.radians(angle)) * 1032
        y = player_coord[1] + math.sin(math.radians(angle)) * 1032
        pygame.draw.line(screen, "red", player_coord, (x, y))

        # Отображение изменений на экране
        pygame.display.flip()

        # Задержка времени для управления FPS
        clock.tick(FPS)

    # Завершение работы Pygame
    pygame.quit()
    sys.exit()
