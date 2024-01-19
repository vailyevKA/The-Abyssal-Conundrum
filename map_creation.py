import pygame
import sqlite3
import csv



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
        with open('map_out.csv', 'w', newline='') as f:
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


def makemap():
    print(
        'Преветствуем вас в редакторе карт для игры The Abyssal Conundrum, настоятельно рекомендуем изучить файл README. Если после ввода вам кажется, что программа не работает, посмотрите, не свернулась ли она.')
    pygame.init()
    a, b = list(map(int, input(
        'Введите количество клеток без учёта стенок сначала по вертикали, потом по горизонтали через пробел\n>>').split()))
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

        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()


'''def load_map_from_csv(filepath):
    con = sqlite3.connect(f"settings.db")
    cur = con.cursor()
    cur.execute(f"""UPDATE Game_mode SET game_mode = {1}""")
    con.commit()
    con.close()

    try:
        with open(filepath, 'r', newline='') as f:
            reader = csv.reader(f)
            map_world = [list(map(int, row)) for row in reader]
            for row in map_world:
                row.insert(0, 1)
                row.append(1)
            map_world.insert(0, [1] * len(map_world[0]))
            map_world.append([1] * len(map_world[0]))
        return map_world
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
        return []'''


