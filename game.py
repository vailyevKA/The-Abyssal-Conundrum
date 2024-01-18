import pygame
import sys
from raycasing import *
from mini_map_draw import *
from collisions import can_go
from bot import find_target, is_bot_see_player
from settings import *


def game(line_y2=150):
    # Pygame initialization
    pygame.init()

    # Window creation
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Abyssal conundrum")

    # Initialization of time variables and FPS
    clock = pygame.time.Clock()

    running = True

    mot_w = False
    mot_s = False

    rot_r = False
    rot_l = False

    angle = 180

    shift_event = False

    bot_target = [[], []]

    targ = find_target()

    bot_target[0] = targ[0]
    bot_target[1] = targ[1]
    way = targ[2]

    # The main game cycle

    while running:
        screen.fill("grey")
        pygame.draw.rect(screen, (65, 105, 225), (0, 0, WIDTH, HEIGHT / 2))
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

                if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                    shift_event = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    mot_w = False

                if event.key == pygame.K_s:
                    mot_s = False

                if event.key == pygame.K_d:
                    rot_r = False

                if event.key == pygame.K_a:
                    rot_l = False

                if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                    shift_event = False

        # In the function can_go() the last argument is the player’s direction. True - forward; False - backward

        if mot_w and can_go(player_coord[0], player_coord[1], angle, True, player_speed) and (
                not shift_event or shift_event and line_y2 < 20):
            player_coord[0] += (minimap_size / 30) * (math.cos(math.radians(angle))) * player_speed
            player_coord[1] += (minimap_size / 30) * (math.sin(math.radians(angle))) * player_speed

        if mot_s and can_go(player_coord[0], player_coord[1], angle, False, player_speed) and (
                not shift_event or shift_event and line_y2 < 20):
            player_coord[0] -= (minimap_size / 30) * (math.cos(math.radians(angle))) * player_speed
            player_coord[1] -= (minimap_size / 30) * (math.sin(math.radians(angle))) * player_speed

        if mot_w and can_go(player_coord[0], player_coord[1], angle, True, shift_speed) and shift_event and 20 < line_y2 < 150:
            player_coord[0] += (minimap_size / 30) * (math.cos(math.radians(angle))) * shift_speed
            player_coord[1] += (minimap_size / 30) * (math.sin(math.radians(angle))) * shift_speed

        if mot_s and can_go(player_coord[0], player_coord[1], angle, False, shift_speed) and shift_event and 20 < line_y2 < 150:
            player_coord[0] -= (minimap_size / 30) * (math.cos(math.radians(angle))) * shift_speed
            player_coord[1] -= (minimap_size / 30) * (math.sin(math.radians(angle))) * shift_speed

        if rot_r:
            angle += mouse_speed * 2
            angle %= 360 * NUM_RAYS

        if rot_l:
            angle -= mouse_speed * 2
            angle %= 360

        if shift_event and line_y2 >= 20:
            line_y2 -= 4

        if line_y2 <= 150 and not shift_event:
            line_y2 += 1

        # mini-map drawing

        ray_casting(screen, player_coord, angle)

        draw_minimap(screen, map_world, minimap_size, player_coord)

        pygame.draw.line(screen, 'red', (len(map_world) * minimap_size + 3.5, 20),
                         (len(map_world) * minimap_size + 3.5, line_y2), 7)

        # bot

        pygame.draw.circle(screen, "red", bot_coord, minimap_size / 5)

        is_bot_agr = is_bot_see_player()
        if not is_bot_agr[0]:
            if int(bot_coord[0]) != int(bot_target[0]) or int(bot_coord[1]) != int(bot_target[1]):
                if way == "right":
                    bot_coord[0] += 1
                if way == "left":
                    bot_coord[0] -= 1
                if way == "up":
                    bot_coord[1] += 1
                if way == "down":
                    bot_coord[1] -= 1

            else:
                targ = find_target()

                bot_target[0] = targ[0]
                bot_target[1] = targ[1]
                way = targ[2]
        else:
            bot_target[0] = is_bot_agr[0]
            bot_target[1] = is_bot_agr[1]
            way = is_bot_agr[2]
            if way == "right":
                bot_coord[0] += 1
            if way == "left":
                bot_coord[0] -= 1
            if way == "up":
                bot_coord[1] += 1
            if way == "down":
                bot_coord[1] -= 1

        # Display changes on the screen
        pygame.display.flip()

        # Time delay for FPS management
        clock.tick(FPS)

    # Shutting down Pygame
    pygame.quit()
    sys.exit()