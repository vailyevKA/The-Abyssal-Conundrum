import math

# game settings
WIDTH, HEIGHT = 896, 512
minimap_size = 30
mouse_speed = 1.7

# player settings
player_coord = [WIDTH // 2, HEIGHT // 2]

# map settings
map_world = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

#ray cating settings
FOV = math.pi / 3 #fild of view
NUM_RAYS = 9 #number of rays
DELTA_ANGLE = FOV / NUM_RAYS #the angle between the beams
MAX_DEPTH = 800 #beam length
HALF_FOV = FOV / 2
