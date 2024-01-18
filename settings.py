import math

# game settings
WIDTH, HEIGHT = 896, 512
minimap_size = 15
mouse_speed = 4
player_speed = 2.5
FPS = 30
shift_control = 130
shift_speed = 4
line_y2 = 150

# player settings
player_coord = [minimap_size * 1.5, minimap_size * 1.5]

# map settings
WALLS_SIZE = 15
map_world = []
with open('map_out.txt') as map:
    map = map.readlines()
    for i in map:
        map_world.append([int(j) for j in i.split()])

# bot settings
bot_coord = [minimap_size / 2 * 7, minimap_size / 2 * 5]
bot_angle = 0
bot_speed = 0.5

# raycasting settings
FOV = math.pi / 3  # field of view
NUM_RAYS = 151  # number of rays
DELTA_ANGLE = FOV / NUM_RAYS  # the angle between the beams
MAX_DEPTH = 800  # beam length
HALF_FOV = FOV / 2
