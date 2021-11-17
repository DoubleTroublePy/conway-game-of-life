import numpy as np
import pygame
import sys
import time
import random

pygame.init()

_BLACK = (10, 10, 10)
_DARK_GRAY = (100, 100, 100)
_GRAY = (128, 128, 128)
_WHITE = (200, 200, 200)


def _draw_rectangle(x, y, dim, color, SCREEN):
    rect = pygame.Rect(x * dim, y * dim,
                       (dim-1), (dim-1))
    pygame.draw.rect(SCREEN, color, rect)


class Grid:
    _WINDOW_HEIGHT = 700
    _WINDOW_WIDTH = 700

    _running = True

    def __init__(self, dim):
        self._dim = (dim * dim)
        self._arr = np.array([0] * self._dim)
        self._ready = False

        self._SCREEN = pygame.display.set_mode((self._WINDOW_HEIGHT, self._WINDOW_WIDTH))
        self._CLOCK = pygame.time.Clock()
        self._SCREEN.fill(_WHITE)

        s = int(np.sqrt(self._arr.size))
        self._arr = self._arr.reshape(s, s)
        self._arr2 = self._arr.copy()

        self.draw_grid()

    def run(self):
        s = int(np.sqrt(self._arr.size))
        self._arr = self._arr.reshape(s, s)
        self._arr2 = self._arr.copy()

        self.draw_grid()
        while True:
            if self._ready:
                # game loop
                for x in range(len(self._arr)):
                    for y in range(len(self._arr[0])):
                        if self._arr[y][x]:
                            _draw_rectangle(x, y, self._WINDOW_WIDTH / len(self._arr), _BLACK, self._SCREEN)
                        else:
                            _draw_rectangle(x, y, self._WINDOW_WIDTH / len(self._arr), _WHITE, self._SCREEN)

                self.evolve()
                self._arr = self._arr2.copy()
                time.sleep(.25)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    pos_y = int((y * len(self._arr2)) / self._WINDOW_HEIGHT)
                    pos_x = int((x * len(self._arr2)) / self._WINDOW_WIDTH)
                    if self._arr[pos_y][pos_x] == 0:
                        _draw_rectangle(pos_x, pos_y, self._WINDOW_WIDTH / len(self._arr), _BLACK, self._SCREEN)
                        self._arr[pos_y][pos_x] = 1
                        self._arr2[pos_y][pos_x] = 1
                    else:
                        _draw_rectangle(pos_x, pos_y, self._WINDOW_WIDTH / len(self._arr), _WHITE, self._SCREEN)
                        self._arr[pos_y][pos_x] = 0
                        self._arr2[pos_y][pos_x] = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self._ready = not self._ready
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    if event.key == pygame.K_r:
                        self._arr = np.array([0] * self._dim)
                        s = int(np.sqrt(self._arr.size))
                        self._arr = self._arr.reshape(s, s)
                    if event.key == pygame.K_c:
                        self._arr = np.array([0] * self._dim)
                        for i in range(len(self._arr)):
                            self._arr[i] = random.randint(0, 1)
                        s = int(np.sqrt(self._arr.size))
                        self._arr = self._arr.reshape(s, s)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def resize(self, height, width):
        self._SCREEN.fill(_WHITE)
        self._WINDOW_HEIGHT = height
        self._WINDOW_WIDTH = width
        self._SCREEN = pygame.display.set_mode((self._WINDOW_HEIGHT, self._WINDOW_WIDTH))
        self.draw_grid()
        pygame.display.update()

    def evolve(self):
        for y in range(len(self._arr2)):
            for x in range(len(self._arr2[0])):
                neigh = self.n_neighbors(x, y)
                if self._arr2[y][x]:
                    if neigh < 2:
                        self._arr2[y][x] = 0
                    if neigh > 3:
                        self._arr2[y][x] = 0
                    if neigh == 3:
                        self._arr2[y][x] = 1
                elif neigh == 3:
                    self._arr2[y][x] = 1

    def n_neighbors(self, x, y):
        neigh = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                # print(('%2i %2i') % (x + i, y + j))
                if not (i == 0 and j == 0) and (y + i) < len(self._arr) and (x + j) < len(self._arr) and \
                        (y + i) > 0 and (x + j) > 0 and self._arr[y + i][x + j] == 1:
                    neigh += 1
        # print('-----')
        return neigh

    def draw_grid(self):
        block_size = self._WINDOW_WIDTH / len(self._arr)  # Set the size of the grid block
        for x in range(self._WINDOW_WIDTH):
            for y in range(self._WINDOW_HEIGHT):
                rect = pygame.Rect(x * block_size, y * block_size,
                                   block_size, block_size)
                pygame.draw.rect(self._SCREEN, _GRAY, rect, 1)
                _draw_rectangle(x, y, self._WINDOW_WIDTH / len(self._arr), _WHITE, self._SCREEN)


class Option:
    pass