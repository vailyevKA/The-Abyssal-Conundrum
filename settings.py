import math
import random
import csv
import sqlite3
# from map_creation import load_map_from_csv
import pygame

# game settings
WIDTH, HEIGHT = 896, 512
minimap_size = 15
mouse_speed = 4
player_speed = 2.5
FPS = 30
shift_control = 130
shift_speed = 4
line_y2 = 150

level = 1

con = sqlite3.connect(f"settings.db")
cur = con.cursor()

result = cur.execute("""SELECT * FROM settings""")

for elem in result:
    level = elem[2]

if level == 2:
    map_world = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                 [1, 0, 2, 1, 0, 1, 0, 1, 2, 1, 0, 1], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1], [1, 1, 1, 0, 0, 0, 2, 0, 1, 1, 0, 1],
                 [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 1, 2, 0, 1, 2, 0, 1, 1, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1], [1, 0, 2, 0, 1, 1, 0, 1, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
if level == 3:
    map_world = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 1, 1, 0, 1],
                 [1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                 [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 0, 2, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 1, 1, 1], [1, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 2, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1], [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                 [1, 0, 0, 0, 0, 0, 1, 0, 1, 2, 0, 1, 0, 0, 1], [1, 0, 1, 1, 0, 0, 2, 0, 0, 0, 0, 1, 0, 1, 1],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
else:
    map_world = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1, 0, 0, 1], [1, 0, 1, 2, 2, 0, 0, 0, 1, 1],
                 [1, 0, 0, 0, 1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 1, 0, 1, 1, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 0, 2, 0, 1, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

con_ = sqlite3.connect(f"settings.db")
cur_ = con_.cursor()


WALLS_SIZE = 15
# map_world = []
# with open('map_out.txt') as map:
#    map = map.readlines()
#    for i in map:
#       map_world.append([int(j) for j in i.split()])


# bot settings
bot_angle = 0
bot_speed = 0.5

# raycasting settings
FOV = math.pi / 3  # field of view

#   number of rays
NUM_RAYS = 151
con_ = sqlite3.connect(f"settings.db")
cur_ = con.cursor()
result_ = cur.execute("""SELECT * FROM graphics""")
for elem_ in result_:
    NUM_RAYS = elem_[0]
if not NUM_RAYS:
    NUM_RAYS = 151

DELTA_ANGLE = FOV / NUM_RAYS  # the angle between the beams
MAX_DEPTH = 800  # beam length
HALF_FOV = FOV / 2

player_coord = [minimap_size * 1.5, minimap_size * 1.5]  # [22.5, 22.5]
r_y = random.randint(1, len(map_world) - 1)
r_x = random.randint(1, len(map_world[0]) - 1)
while map_world[r_y][r_x]:
    r_y = random.randint(1, len(map_world) - 1)
    r_x = random.randint(1, len(map_world[0]) - 1)

bot_coord = [minimap_size * r_y + 0.5 * minimap_size, minimap_size * r_x + 0.5 * minimap_size]

