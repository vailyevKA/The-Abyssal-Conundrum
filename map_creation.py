import copy
import pygame
import random
import csv
import sys


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.wall = 1
        self.wallc = 'white'

    def generate_random_table(self):
        n = self.height
        m = self.width

        total_cells = n * m
        num_zeros = int(total_cells * 0.60)

        level_flat = [0] * num_zeros + [random.choice([1, 2]) for _ in range(total_cells - num_zeros)]

        random.shuffle(level_flat)
        level = [level_flat[i * m:(i + 1) * m] for i in range(n)]

        for i in range(n):
            level[i][0] = level[i][m - 1] = random.choice([1, 2])
        for j in range(m):
            level[0][j] = level[n - 1][j] = random.choice([1, 2])

        self.board = copy.deepcopy(level)

    def render(self, screen):
        color = 1
        for row, row_v in enumerate(self.board):
            col = 0
            for col, col_v in enumerate(row_v):
                clr = 'white' if color else 'black'
                if col_v:
                    rect_width = 0
                    clr = 'white' if self.board[row][col] == 1 else 'purple'
                else:
                    rect_width = 1
                pygame.draw.rect(screen, pygame.Color(clr),
                                 (self.left + col * self.cell_size,
                                  self.top + row * self.cell_size,
                                  self.cell_size,
                                  self.cell_size),
                                 rect_width)
                color = color
            if col % 2 != 0:
                color = color

    def set_view(self, left, top, cell_size):
        self.left, self.top, self.cell_size = left, top, cell_size

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        if self.left < x < self.left + (self.width * self.cell_size):
            cell_x = (x - self.left) // self.cell_size
        else:
            return
        if self.top < y < self.top + (self.height * self.cell_size):
            cell_y = (y - self.top) // self.cell_size
        else:
            return
        return cell_x, cell_y

    def on_click(self, cell_pos):
        if cell_pos is None:
            return
        row, col = cell_pos[::-1]
        if not self.board[row][col]:
            self.board[row][col] = self.wall
        else:
            self.board[row][col] = 0
        with open('save\\map_out.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self.board)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def return_matrix(self):
        return self.board

    def change_color(self, c, wallc):
        self.wall = c
        self.wallc = wallc


def draw_text_input(screen, input_text, font, x, y):
    input_box = pygame.Rect(x, y, 140, 32)
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('gray15')
    color = color_passive
    active = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_passive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return input_text
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

        screen.fill((30, 30, 30))
        txt_surface = font.render(input_text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()


def makemap():
    pygame.init()
    screen = pygame.display.set_mode((300, 100))
    pygame.display.set_caption('Map')
    font = pygame.font.Font(None, 32)

    # Get dimensions from user input
    dimensions = draw_text_input(screen, '', font, 30, 30)
    if dimensions is None:
        pygame.quit()
        return
    try:
        a, b = map(int, dimensions.split())
    except ValueError:
        pygame.quit()
        return

    size = width, height = a * 50 + 40, b * 50 + 40
    screen = pygame.display.set_mode(size)
    board = Board(a, b)
    board.set_view(20, 20, 50)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    board.change_color(2, 'purple')
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    board.change_color(1, 'white')
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    board.generate_random_table()

        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()
