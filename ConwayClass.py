import numpy as np
import pygame


class ConwayClass:
    _BLACK = (10, 10, 10)
    _GRAY = (128, 128, 128)
    _WHITE = (200, 200, 200)
    _WINDOW_HEIGHT = 700
    _WINDOW_WIDTH = 700

    def __init__(self, dim):
        self._dim = (dim * dim)
        self._arr = np.array([0] * self._dim)
        self._ready = False
        pygame.init()
        self._SCREEN = pygame.display.set_mode((self._WINDOW_HEIGHT, self._WINDOW_WIDTH))
        self._CLOCK = pygame.time.Clock()
        self._SCREEN.fill(self._WHITE)
        s = int(np.sqrt(self._arr.size))
        self._arr = self._arr.reshape(s, s)
        self._arr2 = self._arr.copy()
        self.draw_grid()

    def update(self):
        s = self._SCREEN
        pygame.s.update()

    def draw_grid(self):
        block_size = self._WINDOW_WIDTH/len(self._arr)  # Set the size of the grid block
        for x in range(self._WINDOW_WIDTH):
            for y in range(self._WINDOW_HEIGHT):
                rect = pygame.Rect(x * block_size, y * block_size,
                                   block_size, block_size)
                pygame.draw.rect(self._SCREEN, self._GRAY, rect, 1)

    def resize(self, height, width):
        self._WINDOW_HEIGHT = height
        self._WINDOW_WIDTH = width

    def n_neighbors(self, y, x) -> int:
        neighbors = [1, 0, -1]
        neigh = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                # print(('%2i %2i') % (x + i, y + j))
                if not(i == 0 and j == 0) and (y + i) < len(self._arr) and (x + j) < len(self._arr) and \
                        (y + i) > 0 and (x + j) > 0 and self._arr[y + i][x + j] == 1:
                    neigh += 1
        # print('-----')
        return neigh

    def evolve(self):
        for y in range(len(self._arr2)):
            for x in range(len(self._arr2)):
                neigh = self.n_neighbors(y, x)
                if self._arr2[y][x]:
                    if neigh < 2:
                        self._arr2[y][x] = 0
                    if neigh > 3:
                        self._arr2[y][x] = 0
                    if neigh == 3:
                        self._arr2[y][x] = 1
                elif neigh == 3:
                    self._arr2[y][x] = 1

    def draw_rectangle(self, x, y, dim, color):
        rect = pygame.Rect(x * dim, y * dim,
                           (dim-1), (dim-1))
        pygame.draw.rect(self._SCREEN, color, rect)

