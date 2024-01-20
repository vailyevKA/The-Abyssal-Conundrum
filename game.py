import pygame
import sys
from raycasing import *
from mini_map_draw import *
from collisions import can_go
from bot import find_target, is_bot_see_player
from settings import *
from bot import draw_monster
from music import SoundPlayer
import time

import csv


def load_map_from_csv(filepath):
    try:
        with open(filepath, 'r', newline='') as f:
            reader = csv.reader(f)
            map_worldf = [list(map(int, row)) for row in reader]
            for row in map_worldf:
                row.insert(0, 1)
                row.append(1)
            map_worldf.insert(0, [1] * len(map_worldf[0]))
            map_worldf.append([1] * len(map_worldf[0]))
        return map_worldf
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
        return []


def game(new_game=False, my_game=False, line_y2=150):
    if new_game:
        con_ = sqlite3.connect(f"save\\settings.db")
        cur_ = con.cursor()
        cur_.execute(f"""UPDATE settings SET level = {str(1)}""")
        con_.commit()
        con_.close()
        len_map_world = len(map_world)
        for i in range(len_map_world):
            map_world.pop(0)
        map_world.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        map_world.append([1, 0, 0, 0, 0, 0, 1, 0, 0, 1])
        map_world.append([1, 0, 1, 2, 2, 0, 0, 0, 1, 1])
        map_world.append([1, 0, 0, 0, 1, 0, 1, 0, 0, 1])
        map_world.append([1, 0, 0, 1, 1, 0, 1, 1, 0, 1])
        map_world.append([1, 1, 0, 0, 0, 0, 0, 0, 0, 1])
        map_world.append([1, 0, 0, 1, 0, 1, 0, 1, 0, 1])
        map_world.append([1, 0, 0, 2, 0, 1, 0, 1, 0, 1])
        map_world.append([1, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        map_world.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

        player_coord[0] = 22.5
        player_coord[1] = 22.5  # [22.5, 22.5]
        r_y_ = random.randint(1, len(map_world) - 1)
        r_x_ = random.randint(1, len(map_world[0]) - 1)
        while map_world[r_y_][r_x_]:
            r_y_ = random.randint(1, len(map_world) - 1)
            r_x_ = random.randint(1, len(map_world[0]) - 1)

        bot_coord[0] = minimap_size * r_x + 0.5 * minimap_size
        bot_coord[1] = minimap_size * r_y + 0.5 * minimap_size
    # Pygame initialization
    pygame.init()

    # Window creation
    pygame.display.set_mode((WIDTH, HEIGHT + 50))
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

    screen_width, screen_height = 896, 512
    screen = pygame.display.set_mode((screen_width, screen_height))
    play_music = SoundPlayer()
    bt = False

    win = False
    if my_game:
        map = load_map_from_csv('save\\map_out.csv')
        for i in range(len(map_world)):
            map_world.pop(0)
        for i in map:
            map_world.append(i)

    # Monster settings
    monster_scale = 3  # Change this value to scale the size of the monster

    # The main game cycle
    while running:
        screen.fill((70, 68, 71))
        pygame.draw.rect(screen, (71, 42, 63), (0, 0, WIDTH, HEIGHT / 2))

        dist_from_bot_to_plyr = ((bot_coord[0] - player_coord[0]) ** 2 + (bot_coord[1] - player_coord[1]) ** 2) ** 0.5

        # steps sound

        if dist_from_bot_to_plyr < 50 and not bt:
            play_music.pause_music()
            bt = True
            play_music.play_steps('sounds\\music.mp3')
        elif dist_from_bot_to_plyr < 50 and bt:
            pass
        elif dist_from_bot_to_plyr >= 50 and bt:
            bt = False
            play_music.pause_music()
        else:
            bt = False

        # lost
        if dist_from_bot_to_plyr <= 10:
            # LOOSE
            con_ = sqlite3.connect(f"save\\settings.db")
            cur_ = con.cursor()
            cur_.execute(f"""UPDATE settings SET level = {str(1)}""")
            con_.commit()
            con_.close()
            len_map_world = len(map_world)
            for i in range(len_map_world):
                map_world.pop(0)
            map_world.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
            map_world.append([1, 0, 0, 0, 0, 0, 1, 0, 0, 1])
            map_world.append([1, 0, 1, 2, 2, 0, 0, 0, 1, 1])
            map_world.append([1, 0, 0, 0, 1, 0, 1, 0, 0, 1])
            map_world.append([1, 0, 0, 1, 1, 0, 1, 1, 0, 1])
            map_world.append([1, 1, 0, 0, 0, 0, 0, 0, 0, 1])
            map_world.append([1, 0, 0, 1, 0, 1, 0, 1, 0, 1])
            map_world.append([1, 0, 0, 2, 0, 1, 0, 1, 0, 1])
            map_world.append([1, 0, 0, 0, 0, 0, 0, 0, 0, 1])
            map_world.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

            player_coord[0] = 22.5
            player_coord[1] = 22.5  # [22.5, 22.5]
            r_y_ = random.randint(1, len(map_world) - 1)
            r_x_ = random.randint(1, len(map_world[0]) - 1)
            while map_world[r_y_][r_x_]:
                r_y_ = random.randint(1, len(map_world) - 1)
                r_x_ = random.randint(1, len(map_world[0]) - 1)

            bot_coord[0] = minimap_size * r_x + 0.5 * minimap_size
            bot_coord[1] = minimap_size * r_y + 0.5 * minimap_size

            im = pygame.image.load("images\\loose.png")
            screen.blit(pygame.transform.scale(im, (WIDTH, HEIGHT)), (0, 0))
            pygame.display.flip()
            play_music.pause_music()
            play_music.play_steps('sounds\\loose.mp3')
            time.sleep(3)

            break

        # win

        win = False

        if 2 not in map_world:
            _2_not_in_map = True
            for el in map_world:
                if 2 in el:
                    _2_not_in_map = False
            if _2_not_in_map:
                # WIN
                con_ = sqlite3.connect(f"save\\settings.db")
                cur_ = con.cursor()

                player_coord[0] = 22.5
                player_coord[1] = 22.5
                bot_coord[0] = 3 * minimap_size + 0.5 * minimap_size
                bot_coord[1] = 3 * minimap_size + 0.5 * minimap_size

                targ = find_target()

                bot_target[0] = targ[0]
                bot_target[1] = targ[1]
                way = targ[2]

                result_ = cur.execute("""SELECT * FROM settings""")
                level_ = 1
                for elem_ in result_:
                    level_ = elem_[2]
                if level_ is None:
                    level_ = 1
                if level_ <= 3:
                    level_ += 1
                    cur_.execute(f"""UPDATE settings
                                        SET level = {str(level_)}""")
                    con_.commit()
                    con_.close()

                    if level_ == 1:
                        len_map_world = len(map_world)
                        for i in range(len_map_world):
                            map_world.pop(0)
                        map_world.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
                        map_world.append([1, 0, 0, 0, 0, 0, 1, 0, 0, 1])
                        map_world.append([1, 0, 1, 2, 2, 0, 0, 0, 1, 1])
                        map_world.append([1, 0, 0, 0, 1, 0, 1, 0, 0, 1])
                        map_world.append([1, 0, 0, 1, 1, 0, 1, 1, 0, 1])
                        map_world.append([1, 1, 0, 0, 0, 0, 0, 0, 0, 1])
                        map_world.append([1, 0, 0, 1, 0, 1, 0, 1, 0, 1])
                        map_world.append([1, 0, 0, 2, 0, 1, 0, 1, 0, 1])
                        map_world.append([1, 0, 0, 0, 0, 0, 0, 0, 0, 1])
                        map_world.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

                    if level_ == 2:
                        len_map_world = len(map_world)
                        for i in range(len_map_world):
                            map_world.pop(0)
                        map_world.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
                        map_world.append([1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1])
                        map_world.append([1, 0, 2, 1, 0, 1, 0, 1, 2, 1, 0, 1])
                        map_world.append([1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1])
                        map_world.append([1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1])
                        map_world.append([1, 1, 1, 0, 0, 0, 2, 0, 1, 1, 0, 1])
                        map_world.append([1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1])
                        map_world.append([1, 1, 0, 1, 2, 0, 1, 2, 0, 1, 1, 1])
                        map_world.append([1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1])
                        map_world.append([1, 0, 2, 0, 1, 1, 0, 1, 0, 0, 0, 1])
                        map_world.append([1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1])
                        map_world.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

                    if level_ == 3:
                        len_map_world = len(map_world)
                        for i in range(len_map_world):
                            map_world.pop(0)
                        map_world.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
                        map_world.append([1, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 1, 1, 0, 1])
                        map_world.append([1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1])
                        map_world.append([1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1])
                        map_world.append([1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1])
                        map_world.append([1, 1, 1, 0, 2, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1])
                        map_world.append([1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 1, 1, 1])
                        map_world.append([1, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
                        map_world.append([1, 0, 0, 0, 2, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1])
                        map_world.append([1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1])
                        map_world.append([1, 0, 0, 0, 0, 0, 1, 0, 1, 2, 0, 1, 0, 0, 1])
                        map_world.append([1, 0, 1, 1, 0, 0, 2, 0, 0, 0, 0, 1, 0, 1, 1])
                        map_world.append([1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1])
                        map_world.append([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1])
                        map_world.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

                    targ = find_target()

                    bot_target[0] = targ[0]
                    bot_target[1] = targ[1]
                    way = targ[2]

                    im = pygame.image.load("images\\win.png")
                    screen.blit(pygame.transform.scale(im, (WIDTH, HEIGHT)), (0, 0))
                    pygame.display.flip()
                    play_music.pause_music()
                    play_music.play_steps('sounds\\win.mp3')
                    time.sleep(1.5)

                else:
                    cur_.execute(f"""UPDATE settings
                                        SET level = {"1"}""")
                    con_.commit()
                    con_.close()
                    break

        # event processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    mot_w = True
                    if not bt:
                        play_music.play_steps('sounds\\steps.mp3')

                if event.key == pygame.K_s:
                    mot_s = True
                    if not bt:
                        play_music.play_steps('sounds\\steps.mp3')

                if event.key == pygame.K_d:
                    rot_r = True

                if event.key == pygame.K_a:
                    rot_l = True

                if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                    shift_event = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    mot_w = False
                    if not bt:
                        play_music.pause_music()

                if event.key == pygame.K_s:
                    mot_s = False
                    if not bt:
                        play_music.pause_music()

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

        if mot_w and can_go(player_coord[0], player_coord[1], angle, True,
                            shift_speed) and shift_event and 20 < line_y2 < 150:
            player_coord[0] += (minimap_size / 30) * (math.cos(math.radians(angle))) * shift_speed
            player_coord[1] += (minimap_size / 30) * (math.sin(math.radians(angle))) * shift_speed

        if mot_s and can_go(player_coord[0], player_coord[1], angle, False,
                            shift_speed) and shift_event and 20 < line_y2 < 150:
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
                    bot_coord[0] += bot_speed
                if way == "left":
                    bot_coord[0] -= bot_speed
                if way == "up":
                    bot_coord[1] += bot_speed
                if way == "down":
                    bot_coord[1] -= bot_speed

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
                bot_coord[0] += bot_speed
            if way == "left":
                bot_coord[0] -= bot_speed
            if way == "up":
                bot_coord[1] += bot_speed
            if way == "down":
                bot_coord[1] -= bot_speed

        # Display changes on the screen
        pygame.display.flip()

        # Time delay for FPS management
        clock.tick(FPS)

    # Shutting down Pygame
    pygame.quit()
