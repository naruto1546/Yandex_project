import pygame


class Board:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.board = [[0] * w for _ in range(h)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.GREY = pygame.Color('#DBD7D2')

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, surface):

        for i in range(self.h):
            for j in range(self.w):
                pygame.draw.rect(surface, self.GREY, (
                    self.left + self.cell_size * j,
                    self.top + self.cell_size * i,
                    self.cell_size, self.cell_size),
                                 1 if self.board[i][j] == 0 else 0)

    def get_click(self, mouse_pos):
        coords = self.get_cell(mouse_pos)
        if coords is None:
            return
        else:
            self.click(coords)

    def get_cell(self, mouse_pos):
        board_w = self.w * self.cell_size
        board_h = self.h * self.cell_size
        if self.left < mouse_pos[0] < self.left + board_w:
            if self.top < mouse_pos[1] < self.top + board_h:
                coords = (mouse_pos[1] - self.left) // self.cell_size, \
                         (mouse_pos[0] - self.top) // self.cell_size
                return coords
        return None

    def click(self, coords):
        i = coords[0] // self.left - 1
        j = coords[1] // self.top - 1
        if (i >= 0 and j >= 0) and (i <= self.w and j <= self.h):
            i = coords[0] // self.left - 1
            j = coords[1] // self.top - 1
            print((i, j))
        else:
            print(None)
