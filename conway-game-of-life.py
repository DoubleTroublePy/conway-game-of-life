import numpy as np
import pygame
import random
import time
import sys

BLACK = (10, 10, 10)
GRAY = (128, 128, 128)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 700
WINDOW_WIDTH = 700


def n_neighbors(arr: np.ndarray, y, x) -> int:
    neighbors = [1, 0, -1]
    neigh = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            # print(('%2i %2i') % (x + i, y + j))
            if not(i == 0 and j == 0) and (y + i) < len(arr) and (x + j) < len(arr) and \
                    (y + i) > 0 and (x + j) > 0 and arr[y + i][x + j] == 1:
                neigh += 1
    # print('-----')
    return neigh


def frame(arr: np.ndarray) -> np.ndarray:
    for y in range(len(arr2)):
        for x in range(len(arr2)):
            neigh = n_neighbors(arr, y, x)
            # print(neigh, end=' ')
            if arr2[y][x]:
                if neigh < 2:
                    arr2[y][x] = 0
                if neigh > 3:
                    arr2[y][x] = 0
                if neigh == 3:
                    arr2[y][x] = 1
            elif neigh == 3:
                arr2[y][x] = 1
    # print()
    return arr2



def draw_grid():
    block_size = WINDOW_WIDTH/len(arr)  # Set the size of the grid block
    for x in range(WINDOW_WIDTH):
        for y in range(WINDOW_HEIGHT):
            rect = pygame.Rect(x * block_size, y * block_size,
                               block_size, block_size)
            pygame.draw.rect(SCREEN, GRAY, rect, 1)


def draw_rectangle(x, y, dim, color):
    rect = pygame.Rect(x * dim, y * dim,
                       (dim-1), (dim-1))
    pygame.draw.rect(SCREEN, color, rect)


if __name__ == '__main__':
    dim = 50 * 50
    arr = np.array([0] * dim)
    ready = False

    # setup
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)
    s = int(np.sqrt(arr.size))
    arr = arr.reshape(s, s)
    arr2 = arr.copy()
    draw_grid()

    while True:
        if not ready:
            pass
        if ready:
            # game loop
            for x in range(len(arr)):
                for y in range(len(arr[0])):
                    if arr[y][x]:
                        draw_rectangle(x, y, WINDOW_WIDTH / len(arr), BLACK)
                    else:
                        draw_rectangle(x, y, WINDOW_WIDTH / len(arr), WHITE)

            arr2 = frame(arr)
            arr = arr2.copy()
            time.sleep(.25)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # print('click..%d..%d' % (int((x*len(arr2))/WINDOW_HEIGHT), int((y*len(arr2))/WINDOW_WIDTH)) )
                if arr[int((y*len(arr2))/WINDOW_HEIGHT)][int((x*len(arr2))/WINDOW_WIDTH)] == 0:
                    draw_rectangle(int((x*len(arr2))/WINDOW_HEIGHT), int((y*len(arr2))/WINDOW_WIDTH),
                                   WINDOW_WIDTH / len(arr), BLACK)
                    arr[int((y*len(arr2))/WINDOW_HEIGHT)][int((x*len(arr2))/WINDOW_WIDTH)] = 1
                    arr2[int((y*len(arr2))/WINDOW_HEIGHT)][int((x*len(arr2))/WINDOW_WIDTH)] = 1
                else:
                    draw_rectangle(int((x*len(arr2))/WINDOW_HEIGHT), int((y*len(arr2))/WINDOW_WIDTH),
                                   WINDOW_WIDTH / len(arr), WHITE)
                    arr[int((y*len(arr2))/WINDOW_HEIGHT)][int((x*len(arr2))/WINDOW_WIDTH)] = 0
                    arr2[int((y*len(arr2))/WINDOW_HEIGHT)][int((x*len(arr2))/WINDOW_WIDTH)] = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ready = not ready
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_r:
                    arr = np.array([0] * dim)
                    s = int(np.sqrt(arr.size))
                    arr = arr.reshape(s, s)
                if event.key == pygame.K_c:
                    arr = np.array([0] * dim)
                    for i in range(len(arr)):
                        arr[i] = random.randint(0, 1)
                    s = int(np.sqrt(arr.size))
                    arr = arr.reshape(s, s)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
