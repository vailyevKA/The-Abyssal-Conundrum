import math

# game settings
WIDTH, HEIGHT = 896, 512
minimap_size = 15
mouse_speed = 2

# player settings
player_coord = [minimap_size * 1.5, minimap_size * 1.5]

# map settings
WALLS_SIZE = 15
map_world = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


# raycasting settings
FOV = math.pi / 3  # field of view
NUM_RAYS = 301  # number of rays
DELTA_ANGLE = FOV / NUM_RAYS  # the angle between the beams
MAX_DEPTH = 800  # beam length
HALF_FOV = FOV / 2

