import pygame


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

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def return_matrix(self):
        return self.board

    def change_color(self, c, wallc):
        self.wall = c
        self.wallc = wallc


def makemap():
    pygame.init()
    a, b = list(
        map(int,
            input('Введите количество клеток сначала по вертикали, потом по горизонтали через пробел\n>>').split()))
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
                with open('map_out.txt', 'w') as f:
                    for i in board.return_matrix():
                        print(*[j if j else 0 for j in i], file=f, end='\n')
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


makemap()



# #вставить вместо задания карты
# with open('map_out.txt', 'r') as f:
#     map_world = [list(map(int, i.split())) for i in f.readlines()]
