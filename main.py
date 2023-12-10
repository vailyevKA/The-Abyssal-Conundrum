import pygame
import sys
from raycasting import *
from mini_map_draw import *
from collisions import can_go

if __name__ == '__main__':
    # Pygame initialization
    pygame.init()

    # Window creation
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Abyssal conundrum")

    # Initialization of time variables and FPS
    clock = pygame.time.Clock()
    FPS = 30

    running = True

    mot_w = False
    mot_s = False
    mot_d = False
    mot_a = False

    rot_r = False
    rot_l = False

    angle = 180

    # The main game cycle

    while running:
        screen.fill("grey")
        pygame.draw.rect(screen, "brown", (0, 0, WIDTH, HEIGHT / 2))
        # event processing
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

        # In the function can_go() the last argument is the player’s direction. True - forward; False - backward

        if mot_w and can_go(player_coord[0], player_coord[1], angle, True):
            player_coord[0] += (minimap_size / 30) * (math.cos(math.radians(angle))) * 1.5
            player_coord[1] += (minimap_size / 30) * (math.sin(math.radians(angle))) * 1.5

        if mot_s and can_go(player_coord[0], player_coord[1], angle, False):
            player_coord[0] -= (minimap_size / 30) * (math.cos(math.radians(angle))) * 1.5
            player_coord[1] -= (minimap_size / 30) * (math.sin(math.radians(angle))) * 1.5

        if rot_r:
            angle += mouse_speed * 2
            angle %= 360 * NUM_RAYS

        if rot_l:
            angle -= mouse_speed * 2
            angle %= 360

        # mini-map drawing

        ray_casting(screen, player_coord, angle)

        draw_minimap(screen, map_world, minimap_size, player_coord)

        # Display changes on the screen
        pygame.display.flip()

        # Time delay for FPS management
        clock.tick(FPS)

    # Shutting down Pygame
    pygame.quit()
    sys.exit()
